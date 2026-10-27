# punlabs.io

Website for Pun Labs LLC, served with GitHub Pages at https://punlabs.io.

- `index.html`: home page
- `brands/`: Pop Colors and the Serious Supply coming-soon section
- `wholesale/`: how to order, plus the wholesale inquiry form (the QR code opens `/wholesale/?src=qr`)
- `about/`, `contact/` (contact form), `thanks/` (shown after a form submission), `404.html`
- `assets/`: logos, styles, icons, sharing image, contact card (.vcf)
- `_build/build.py`: regenerates every page; edit copy there and run `python3 _build/build.py`

Both forms post to the Google Form "Pun Labs Website Form", whose responses land in the Google Sheet "Pun Labs Website Submissions". Product photos load from the Pop Colors Shopify store.
