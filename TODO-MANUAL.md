# TODO-MANUAL.md — Manual Tasks Requiring Human Action

## Phase 0: Bootstrap

- [ ] **Set up OpenRouter account** — Get API key from https://openrouter.ai
- [ ] **Set up Clerk account** — Create application, get API keys
- [ ] **Set up Stripe account** — Create products for token packages
- [ ] **Set up Zep Cloud account** — Get API key for agent memory
- [ ] **Set up MinIO** — Configure buckets for map assets and scenario data
- [ ] **VPS access** — Verify SSH access to Hostinger VPS (168.231.103.49)
- [ ] **Domain setup** — Configure DNS for project domain
- [ ] **SSL certificates** — Set up Let's Encrypt for HTTPS

## Phase 1: Map + Game Shell

- [ ] **Map data** — Download/prepare world_borders.geojson and world_cities.json
- [ ] **Custom map assets** — Create/source maps for Star Wars, Dune, GoT scenarios

## Phase 3: Swarm Engine

- [ ] **Neo4j license** — Verify Community Edition is sufficient for projected graph size
- [ ] **Zep Cloud pricing** — Confirm pricing tier supports expected agent memory volume

## Phase 6: Token Economy

- [ ] **Stripe products** — Create token package products in Stripe dashboard
- [ ] **Pricing strategy** — Finalize token pricing and free tier allocation

## Phase 7: Launch

- [ ] **AWS Mumbai setup** — Create VPC, EC2 instances, RDS, ElastiCache
- [ ] **CDN** — Set up CloudFront for static assets
- [ ] **Monitoring** — Set up Datadog/Grafana for production monitoring
- [ ] **Legal** — Terms of service, privacy policy
- [ ] **IP licensing** — Verify fair use for pop culture scenarios (Star Wars, Dune, GoT)
