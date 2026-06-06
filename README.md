# Smash Burgery — Forest Hill

Single-page marketing website for **Smash Burgery**, a 100% halal smash burger and Nashville hot chicken joint at 342-348 Springvale Rd, Forest Hill VIC 3131.

## Stack
- Single static `index.html` (inline CSS + vanilla JS, no build step, no framework)
- Google Fonts: Anton (display) + Inter (body)
- Responsive WebP imagery in `assets/`
- Instagram reel embed + Google Maps embed
- LocalBusiness / Restaurant JSON-LD for local SEO
- Open Graph + Twitter share cards

## Run locally
```bash
python -m http.server 5500
# open http://localhost:5500
```

## Brand
- Black + bright green (`#4fd13b` accent, `#6ee85a` highlight) on charcoal, cream text

## Before going live (owner)
- [ ] Confirm the production **domain** (currently assumes `smashburgery.com.au` in canonical / JSON-LD / robots)
- [ ] Add a **phone number** to the JSON-LD if desired
- [ ] Click-test the **DoorDash** link (an older "Shipoopis Smash Burgers" listing exists at the same address)
- [ ] Swap AI-enhanced food renders for the owner's real high-res photos when available

## Order links
- Uber Eats: https://www.ubereats.com/au/store/smash-burgery/4F7Kjc2nQSiI8r-2Mi3mWw
- DoorDash: https://www.doordash.com/store/smash-burgery-forest-hill-39355169/
- Instagram: https://instagram.com/smashburgery

Built by Vanguard Digital.
