import Stripe from "stripe";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

// TODO: Set STRIPE_SECRET_KEY in environment variables
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY ?? "sk_test_placeholder", {
  apiVersion: "2024-12-18.acacia",
});

export interface CheckoutParams {
  userId: string;
  email: string;
  packageId: string;
  packageName: string;
  priceInCents: number;
  tokens: number;
}

/**
 * Create a Stripe Checkout session for token purchase.
 */
export async function createCheckoutSession(
  params: CheckoutParams
): Promise<Stripe.Checkout.Session> {
  const { userId, email, packageId, packageName, priceInCents, tokens } = params;

  const session = await stripe.checkout.sessions.create({
    payment_method_types: ["card"],
    mode: "payment",
    customer_email: email,
    line_items: [
      {
        price_data: {
          currency: "usd",
          product_data: {
            name: packageName,
            description: `${tokens} tokens for Project Nexus`,
          },
          unit_amount: priceInCents,
        },
        quantity: 1,
      },
    ],
    metadata: {
      userId,
      packageId,
      tokens: tokens.toString(),
    },
    success_url: `${process.env.FRONTEND_URL ?? "http://localhost:3000"}/tokens/success?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${process.env.FRONTEND_URL ?? "http://localhost:3000"}/tokens/cancel`,
  });

  return session;
}

/**
 * Handle Stripe webhook events (checkout.session.completed, etc.).
 * Should be called from a dedicated webhook route.
 */
export async function handleStripeWebhook(
  rawBody: string,
  signature: string
): Promise<void> {
  const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

  if (!webhookSecret) {
    throw new Error("STRIPE_WEBHOOK_SECRET is not configured");
  }

  const event = stripe.webhooks.constructEvent(rawBody, signature, webhookSecret);

  switch (event.type) {
    case "checkout.session.completed": {
      const session = event.data.object as Stripe.Checkout.Session;
      const userId = session.metadata?.["userId"];
      const tokens = parseInt(session.metadata?.["tokens"] ?? "0", 10);
      const packageId = session.metadata?.["packageId"] ?? "unknown";

      if (!userId || tokens <= 0) {
        console.error("Invalid checkout session metadata", session.metadata);
        return;
      }

      // Credit tokens to user account
      await prisma.$transaction([
        prisma.user.update({
          where: { id: userId },
          data: { tokens: { increment: tokens } },
        }),
        prisma.tokenTransaction.create({
          data: {
            userId,
            amount: tokens,
            type: "PURCHASE",
            metadata: {
              stripeSessionId: session.id,
              packageId,
              amountPaid: session.amount_total,
            },
          },
        }),
      ]);

      console.log(`Credited ${tokens} tokens to user ${userId}`);
      break;
    }

    // TODO: Handle refunds, disputes, etc.
    // case "charge.refunded": { ... }

    default:
      console.log(`Unhandled Stripe event: ${event.type}`);
  }
}
