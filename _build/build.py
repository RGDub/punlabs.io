"""Build the punlabs.io static site into /home/claude/punlabs-site."""
import html
import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://punlabs.io"
EMAIL = "grant.weatherford@punlabs.io"
FORM_ID = "1FAIpQLSdzqP79jj9sKe_blDyuMR0y6KCQtP8lm_nEEzfKZQNMfw2NzA"
ACTION = f"https://docs.google.com/forms/d/e/{FORM_ID}/formResponse"
E = {"form": 1083533469, "name": 1711805956, "email": 310555277, "company": 286421248,
     "website": 2095787260, "city": 1848903213, "buy": 1097695607, "topic": 1877716937,
     "message": 8622245, "source": 866755463}

LINKS = {
    "shop": "https://popcolors.com",
    "amazon": "https://www.amazon.com/stores/PunLabs/page/1FCDCFCA-E3FC-4264-9BB8-7B351B1F1EA2",
    "etsy": "https://www.etsy.com/shop/PopColorsCo",
    "faire": "https://www.faire.com/brand/b_22gfmg8kfx",
    "ubc": "https://ubenefit.co",
    "instagram": "https://www.instagram.com/popcolorsco/",
}

CDN = "https://cdn.shopify.com/s/files/1/1906/8217/"
# Real products from the Pop Colors Shopify store (title shortened to the product's own name).
PRODUCTS = [
    ("Office Colors", "12 foil-stamped colored pencils", "office-colors-pencils", "products/OfficeColors1.jpg?v=1633553019"),
    ("Stranger Colors", "12 foil-stamped colored pencils", "stranger-colors-pencils", "products/StrangerColors1.jpg?v=1633553203"),
    ("Van Gogh Colors", "Pencils and coloring pages", "van-gogh-colors-bundle", "files/VanGogh-BlisterPack.jpg?v=1693964331"),
    ("K-Pop Color Hunters", "12 foil-stamped colored pencils", "k-pop-color-hunters-colored-pencil-set-for-fans-of-k-pop-demon-hunters", "files/KPopColorHunters_ListingImages_01.jpg?v=1759277108"),
    ("Colorcraft", "12 foil-stamped colored pencils", "colorcraft-colored-pencils-set", "products/ColorCraft-ProductImages1.jpg?v=1633719598"),
    ("Colors and Recreation", "Pencils and coloring pages", "colors-and-recreation-pages-bundle", "products/Colors-and-Rec-Bundle1.jpg?v=1634842418"),
    ("The One With The Colors", "12 foil-stamped colored pencils", "the-one-with-the-colors-pencils", "files/Friends-1_88a293d4-bd00-48e6-8542-6087da0b3951.jpg?v=1700678183"),
    ("Monet Colors", "Pencils and coloring pages", "monet-colors-bundle", "files/Monet-BlisterPack.jpg?v=1693964419"),
]

PENCIL_COLORS = [  # body, top facet, bottom facet
    ("#7A489C", "#9468B4", "#5E3479"),
    ("#E8453C", "#F06A62", "#C4302A"),
    ("#F28C28", "#F6A657", "#D3721A"),
    ("#2FA84F", "#52BE6F", "#21863C"),
    ("#2C6BE0", "#5487E8", "#1F53B4"),
    ("#8E00D7", "#A733E2", "#7000AA"),
]

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<rect width="64" height="64" rx="12" fill="#7A489C"/>'
           '<path fill="#fff" transform="translate(14.5 57) scale(0.85)" d="M 27.5 -49.875 L 5.90625 -49.875 L 5.90625 0 '
           'L 17.453125 0 L 17.453125 -13.75 L 27.5 -13.75 C 40.828125 -13.75 49.15625 -20.65625 49.15625 -31.78125 '
           'C 49.15625 -42.96875 40.828125 -49.875 27.5 -49.875 Z M 26.859375 -23.15625 L 17.453125 -23.15625 '
           'L 17.453125 -40.46875 L 26.859375 -40.46875 C 33.921875 -40.46875 37.484375 -37.265625 37.484375 -31.78125 '
           'C 37.484375 -26.359375 33.921875 -23.15625 26.859375 -23.15625 Z"/></svg>')


def pencil(text, colors, length=100, tone="foil", font="Montserrat", base=600):
    """A hexagonal pencil seen from the side, pointing right, with its stamp along the barrel."""
    body, top, bot = colors
    w = base * length / 100
    bx = w - 70  # where the sharpened cone starts
    stamp = "#F4EFE2" if tone == "foil" else "#1B1B1B"
    weight = "600" if font == "Montserrat" else "700"
    ls = "2.2" if font == "Montserrat" else "1"
    return f'''<svg class="pencil" viewBox="0 0 {w:.0f} 44" width="{w:.0f}" height="44" role="img" aria-label="{html.escape(text)}" style="--len:{length}%">
<rect x="0" y="4" width="{bx:.0f}" height="36" fill="{body}"/>
<rect x="0" y="4" width="{bx:.0f}" height="10" fill="{top}"/>
<rect x="0" y="30" width="{bx:.0f}" height="10" fill="{bot}"/>
<rect x="0" y="4" width="10" height="36" fill="{bot}" opacity=".55"/>
<polygon points="{bx:.0f},4 {w-22:.0f},18 {w-22:.0f},26 {bx:.0f},40" fill="#E9C9A0"/>
<polygon points="{bx:.0f},4 {w-22:.0f},18 {w-22:.0f},22 {bx:.0f},14" fill="#F2D9B6"/>
<polygon points="{w-22:.0f},18 {w:.0f},22 {w-22:.0f},26" fill="{body}"/>
<text x="34" y="27.5" font-family="{font}, sans-serif" font-size="13" font-weight="{weight}" letter-spacing="{ls}" fill="{stamp}">{html.escape(text)}</text>
</svg>'''


CSS = r"""
:root{
  --ink:#231F20; --muted:#5A5560; --line:#DCD7E1; --paper:#FFFFFF; --mist:#F3F0F6;
  --punlabs:#7A489C; --punlabs-dark:#5E3479; --pop:#8E00D7;
  --steel:#E3E5E6; --steel-ink:#1B1B1B; --legal:#F7E9A0;
  --radius:10px; --wrap:1120px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:Montserrat,system-ui,-apple-system,"Segoe UI",sans-serif;font-size:17px;line-height:1.6;font-weight:400}
img,svg{max-width:100%;height:auto}
a{color:var(--punlabs-dark);text-underline-offset:3px}
a:hover{color:var(--pop)}
:focus-visible{outline:3px solid var(--pop);outline-offset:3px;border-radius:4px}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 16px}
@media(min-width:720px){.wrap{padding:0 32px}}
.skip{position:absolute;left:-9999px}
.skip:focus{left:16px;top:12px;background:#fff;padding:8px 12px;z-index:10}

/* header */
.site-head{border-bottom:1px solid var(--line);background:#fff}
.head-in{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px 24px;padding-top:14px;padding-bottom:14px}
.brand{display:block;line-height:0}
.brand img{width:168px;height:auto}
.nav{display:flex;flex-wrap:wrap;align-items:center;gap:4px 6px;margin:0 -10px;padding:0;list-style:none}
.nav a{display:inline-block;padding:10px;color:var(--ink);text-decoration:none;font-weight:500;font-size:15px}
.nav a:hover{color:var(--pop)}
.nav a[aria-current=page]{color:var(--punlabs);text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:6px}
.nav .nav-cta{background:var(--punlabs);color:#fff;border-radius:999px;padding:9px 18px;margin-left:4px}
.nav .nav-cta:hover{background:var(--punlabs-dark);color:#fff}
.nav .nav-cta[aria-current=page]{text-decoration:none;background:var(--punlabs-dark);color:#fff}
@media(max-width:560px){.head-in{flex-direction:column;align-items:flex-start}.nav{margin:0 -10px}}

/* type */
h1,h2,h3{font-weight:800;line-height:1.12;letter-spacing:-.01em;margin:0 0 .5em}
h1{font-size:clamp(36px,7vw,64px)}
h2{font-size:clamp(26px,4.2vw,38px)}
h3{font-size:20px;font-weight:700;letter-spacing:0}
p{margin:0 0 1em;max-width:62ch}
.lede{font-size:clamp(18px,2.2vw,21px);line-height:1.55;font-weight:400;color:var(--ink)}
.muted{color:var(--muted)}
.small{font-size:15px}

/* buttons */
.btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:50px;padding:12px 24px;border-radius:999px;font-weight:700;font-size:16px;text-decoration:none;border:2px solid var(--punlabs);background:var(--punlabs);color:#fff;font-family:inherit;cursor:pointer}
.btn:hover{background:var(--punlabs-dark);border-color:var(--punlabs-dark);color:#fff}
.btn.ghost{background:transparent;color:var(--punlabs-dark)}
.btn.ghost:hover{background:var(--mist);color:var(--punlabs-dark)}
@media(max-width:480px){.btns .btn{width:100%}}

/* sections */
section{padding:64px 0}
@media(min-width:900px){section{padding:88px 0}}
.band{background:var(--mist)}
.section-head{max-width:720px;margin-bottom:32px}

/* hero */
.hero{padding:48px 0 56px;overflow:hidden}
@media(min-width:900px){.hero{padding:72px 0 88px}}
.hero-grid{display:grid;gap:40px;align-items:center}
@media(min-width:900px){.hero-grid{grid-template-columns:1.05fr 1fr;gap:56px}}
.tag{display:inline-block;font-weight:700;color:var(--punlabs);font-size:16px;margin-bottom:14px}
.pencils{display:flex;flex-direction:column;gap:10px}
.pencils .pencil{display:block;width:var(--len);height:auto}
.pencils .pencil:nth-child(even){margin-left:auto}
@media (prefers-reduced-motion:no-preference){
  .pencils .pencil{animation:slide .7s cubic-bezier(.2,.7,.2,1) both}
  .pencils .pencil:nth-child(2){animation-delay:.06s}.pencils .pencil:nth-child(3){animation-delay:.12s}
  .pencils .pencil:nth-child(4){animation-delay:.18s}.pencils .pencil:nth-child(5){animation-delay:.24s}
  .pencils .pencil:nth-child(6){animation-delay:.3s}
  @keyframes slide{from{transform:translateX(-40px);opacity:0}to{transform:none;opacity:1}}
}

/* products */
.products{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px 16px;margin:0;padding:0;list-style:none}
@media(min-width:720px){.products{grid-template-columns:repeat(3,minmax(0,1fr));gap:28px 24px}}
@media(min-width:1000px){.products.four{grid-template-columns:repeat(4,minmax(0,1fr))}}
.product a{display:block;color:var(--ink);text-decoration:none}
.product .ph{aspect-ratio:1/1;background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.product img{width:100%;height:100%;object-fit:cover;display:block}
.product h3{font-size:16px;margin:12px 0 2px}
.product p{font-size:14px;color:var(--muted);margin:0}
.product a:hover h3{color:var(--pop)}

/* channels */
.channels{display:grid;gap:16px;margin:0;padding:0;list-style:none}
@media(min-width:720px){.channels{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1000px){.channels{grid-template-columns:repeat(4,1fr)}}
.channel a{display:flex;flex-direction:column;height:100%;padding:22px;border:1px solid var(--line);border-radius:var(--radius);background:#fff;color:var(--ink);text-decoration:none}
.channel a:hover{border-color:var(--punlabs)}
.channel strong{font-size:18px;font-weight:700;margin-bottom:4px}
.channel span{font-size:15px;color:var(--muted)}
.channel .go{margin-top:auto;padding-top:14px;color:var(--punlabs-dark);font-weight:600;font-size:15px}

/* wholesale strip */
.strip{background:var(--punlabs);color:#fff}
.strip h2{color:#fff}
.strip p{color:#F1E9F7}
.strip .btn{background:#fff;color:var(--punlabs-dark);border-color:#fff}
.strip .btn:hover{background:var(--mist);border-color:var(--mist)}
.strip .btn.ghost{background:transparent;color:#fff;border-color:#fff}
.strip .btn.ghost:hover{background:rgba(255,255,255,.12)}

/* split blocks */
.split{display:grid;gap:32px}
@media(min-width:900px){.split{grid-template-columns:1fr 1fr;gap:56px}}
.brand-mark{width:260px;max-width:70%;margin-bottom:22px}
.facts{margin:0 0 1em;padding-left:20px}
.facts li{margin-bottom:6px}

/* serious supply */
.serious{background:var(--steel);color:var(--steel-ink)}
.serious h2,.serious h3,.serious p,.serious .typed{font-family:"Courier Prime","Courier New",monospace;letter-spacing:0}
.serious h2{font-weight:700;font-size:clamp(30px,5vw,44px)}
.serious .soon{display:inline-block;border:2px solid var(--steel-ink);padding:4px 10px;font-family:"Courier Prime","Courier New",monospace;font-weight:700;font-size:15px;margin-bottom:18px}
.memo{background:var(--legal);background-image:repeating-linear-gradient(to bottom,transparent 0 29px,#C9D7E8 29px 30px);border-left:3px solid #E58C8C;padding:22px 20px 18px 26px;border-radius:2px;max-width:560px;box-shadow:0 1px 0 rgba(0,0,0,.08)}
.memo p{line-height:30px;margin:0;font-size:16px}
.serious .pencils .pencil:nth-child(even){margin-left:0}
.serious .pencils{gap:12px;margin-top:8px}
.designs{margin-top:56px}
.designs h3{font-size:24px;margin-bottom:4px}
.design-list{list-style:none;margin:20px 0 0;padding:0;display:grid;gap:28px}
@media(min-width:900px){.design-list{grid-template-columns:repeat(3,1fr);gap:32px}}
.design-list li{border-top:2px solid var(--steel-ink);padding-top:18px}
.design-list .gpencil{display:block;width:100%;height:auto}
.design-list p{margin:12px 0 0;font-size:15px;line-height:1.5}

/* pneumart */
.pneumart{background:#F4F0E8;color:#3A3A38}
.pneumart .soon{display:inline-block;border:2px solid #B85532;color:#B85532;border-radius:999px;padding:4px 14px;font-weight:600;font-size:15px;margin-bottom:22px}
.pa-word{font-weight:400;font-size:clamp(44px,8vw,84px);letter-spacing:-.01em;line-height:1;margin:0 0 14px;color:#3A3A38}
.pa-word span{color:#B85532;font-weight:600}
.pa-tag{font-size:clamp(20px,2.6vw,26px);font-weight:300;font-style:italic;margin-bottom:18px}
.pneumart a{color:#9A4326}
.pneumart a:hover{color:#B85532}

/* page header */
.page-head{padding:48px 0 8px}
@media(min-width:900px){.page-head{padding:72px 0 16px}}

/* steps (real sequence: how wholesale ordering works) */
.ways{display:grid;gap:20px}
@media(min-width:900px){.ways{grid-template-columns:1fr 1fr}}
.way{border:1px solid var(--line);border-radius:var(--radius);padding:26px;background:#fff}
.way h3{margin-bottom:8px}

/* forms */
.pl-form{display:flex;flex-direction:column;gap:18px;max-width:720px}
.pl-form .row{display:flex;flex-wrap:wrap;gap:18px}
.pl-form .row>div{flex:1 1 260px;min-width:0}
.pl-form label,.pl-form legend{display:block;font-weight:600;font-size:15px;margin-bottom:6px}
.pl-form .opt{font-weight:400;color:var(--muted)}
.pl-form input[type=text],.pl-form input[type=email],.pl-form input[type=url],.pl-form select,.pl-form textarea{width:100%;font:inherit;font-size:16px;color:var(--ink);background:#fff;border:1px solid #9C95A4;border-radius:8px;padding:12px;min-height:50px}
.pl-form textarea{min-height:130px;resize:vertical}
.pl-form input:focus,.pl-form select:focus,.pl-form textarea:focus{outline:3px solid rgba(142,0,215,.35);border-color:var(--punlabs)}
.pl-form fieldset{border:0;margin:0;padding:0}
.choices{display:flex;flex-wrap:wrap;gap:10px}
.choices label{display:flex;align-items:center;gap:10px;margin:0;font-weight:500;border:1px solid #9C95A4;border-radius:8px;padding:12px 14px;min-height:50px;cursor:pointer;flex:1 1 200px}
.choices input{width:20px;height:20px;accent-color:var(--punlabs);margin:0}
.choices label:has(input:checked){border-color:var(--punlabs);background:var(--mist)}
.pl-form .hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.pl-form .err{display:none;margin:0;padding:12px;border-radius:8px;background:#FDECEC;color:#8A1C1C;font-size:15px}
.pl-form button[disabled]{opacity:.7;cursor:progress}
.form-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px}
@media(min-width:720px){.form-card{padding:36px}}

/* about */
.person{display:flex;gap:18px;align-items:flex-start;margin-top:8px}
.initials{flex:0 0 64px;height:64px;border-radius:50%;background:var(--punlabs);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:22px}

/* footer */
.site-foot{border-top:1px solid var(--line);padding:40px 0 48px;font-size:15px;color:var(--muted)}
.foot-grid{display:grid;gap:24px}
@media(min-width:800px){.foot-grid{grid-template-columns:1.4fr 1fr 1fr}}
.site-foot h2{font-size:15px;font-weight:700;color:var(--ink);margin:0 0 8px;letter-spacing:0}
.site-foot ul{list-style:none;margin:0;padding:0}
.site-foot li{margin-bottom:6px}
.site-foot a{color:var(--ink)}
.site-foot img{width:140px;margin-bottom:12px}
.parent{margin-top:28px;padding-top:18px;border-top:1px solid var(--line)}
"""

FORM_JS = r"""<script>
(function(){
  var params; try{params=new URLSearchParams(location.search);}catch(e){params=null;}
  var topics={wholesale:"Wholesale or volume order",gifting:"Corporate gifting",partner:"Partnership",press:"Press",order:"Question about an order",serious:"Serious Supply updates",pneumart:"PneumART updates"};
  document.querySelectorAll("form[data-pl-form]").forEach(function(form){
    var src=form.querySelector("[data-src]");
    if(params&&src){var s=params.get("src");if(s)src.value=s==="qr"?"QR code":s.slice(0,60);}
    var topic=form.querySelector("select[data-topic]");
    if(params&&topic){var t=topics[params.get("topic")];if(t)topic.value=t;}
    var sink=document.getElementById(form.getAttribute("target"));
    var err=form.querySelector(".err"), btn=form.querySelector("button[type=submit]"), sent=false;
    form.addEventListener("submit",function(ev){
      if(form.querySelector(".hp input").value){ev.preventDefault();return;}
      if(!form.checkValidity()){return;}
      sent=true; btn.disabled=true; btn.textContent="Sending…"; err.style.display="none";
      setTimeout(function(){ if(sent){ sent=false; btn.disabled=false; btn.textContent=btn.getAttribute("data-label"); err.style.display="block"; } },12000);
    });
    sink.addEventListener("load",function(){ if(sent){ sent=false; location.href="/thanks/?f="+encodeURIComponent(form.getAttribute("data-kind")); } });
  });
})();
</script>"""


def field(key):
    return f'entry.{E[key]}'


def wholesale_form():
    return f'''<form class="pl-form" id="ws-form" action="{ACTION}" method="POST" target="ws-sink" data-pl-form data-kind="wholesale">
<input type="hidden" name="{field('form')}" value="Wholesale inquiry">
<input type="hidden" name="{field('source')}" value="Website" data-src>
<div class="hp" aria-hidden="true"><label for="ws-hp">Leave this blank</label><input type="text" id="ws-hp" tabindex="-1" autocomplete="off"></div>
<div class="row">
<div><label for="ws-name">Name</label><input type="text" id="ws-name" name="{field('name')}" autocomplete="name" required maxlength="120"></div>
<div><label for="ws-email">Email</label><input type="email" id="ws-email" name="{field('email')}" autocomplete="email" required maxlength="160"></div>
</div>
<div class="row">
<div><label for="ws-company">Store or company</label><input type="text" id="ws-company" name="{field('company')}" autocomplete="organization" required maxlength="160"></div>
<div><label for="ws-site">Website <span class="opt">(optional)</span></label><input type="text" id="ws-site" name="{field('website')}" autocomplete="url" inputmode="url" maxlength="200" placeholder="yourstore.com"></div>
</div>
<div><label for="ws-city">City and state</label><input type="text" id="ws-city" name="{field('city')}" autocomplete="address-level2" required maxlength="120" placeholder="Asheville, NC"></div>
<fieldset>
<legend>How would you like to buy?</legend>
<div class="choices">
<label><input type="radio" name="{field('buy')}" value="Faire" required> On Faire</label>
<label><input type="radio" name="{field('buy')}" value="Direct"> Directly from Pun Labs</label>
<label><input type="radio" name="{field('buy')}" value="Volume or custom"> Volume or custom order</label>
</div>
</fieldset>
<div><label for="ws-msg">Message <span class="opt">(optional)</span></label><textarea id="ws-msg" name="{field('message')}" maxlength="3000" placeholder="What you'd like to carry, quantities, timing, anything else we should know."></textarea></div>
<p class="err" role="alert">Your inquiry didn't send. Check your connection and try again, or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<div><button class="btn" type="submit" data-label="Send inquiry">Send inquiry</button></div>
<p class="small muted">We reply by email. Your details go only to Pun Labs.</p>
</form>
<iframe name="ws-sink" id="ws-sink" title="Form submission" hidden style="display:none"></iframe>'''


def contact_form():
    opts = ["General question", "Wholesale or volume order", "Corporate gifting", "Partnership", "Press",
            "Question about an order", "Serious Supply updates", "PneumART updates", "Something else"]
    o = "".join(f'<option>{html.escape(x)}</option>' for x in opts)
    return f'''<form class="pl-form" id="ct-form" action="{ACTION}" method="POST" target="ct-sink" data-pl-form data-kind="contact">
<input type="hidden" name="{field('form')}" value="Contact">
<input type="hidden" name="{field('source')}" value="Website" data-src>
<div class="hp" aria-hidden="true"><label for="ct-hp">Leave this blank</label><input type="text" id="ct-hp" tabindex="-1" autocomplete="off"></div>
<div class="row">
<div><label for="ct-name">Name</label><input type="text" id="ct-name" name="{field('name')}" autocomplete="name" required maxlength="120"></div>
<div><label for="ct-email">Email</label><input type="email" id="ct-email" name="{field('email')}" autocomplete="email" required maxlength="160"></div>
</div>
<div class="row">
<div><label for="ct-company">Company <span class="opt">(optional)</span></label><input type="text" id="ct-company" name="{field('company')}" autocomplete="organization" maxlength="160"></div>
<div><label for="ct-topic">What's it about?</label><select id="ct-topic" name="{field('topic')}" data-topic>{o}</select></div>
</div>
<div><label for="ct-msg">Message</label><textarea id="ct-msg" name="{field('message')}" required maxlength="3000"></textarea></div>
<p class="err" role="alert">Your message didn't send. Check your connection and try again, or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<div><button class="btn" type="submit" data-label="Send message">Send message</button></div>
<p class="small muted">Your details go only to Pun Labs. Questions about a Pop Colors order are answered fastest by email.</p>
</form>
<iframe name="ct-sink" id="ct-sink" title="Form submission" hidden style="display:none"></iframe>'''


NAV = [("/brands/", "Brands"), ("/about/", "About"), ("/contact/", "Contact"), ("/wholesale/", "Wholesale")]


def page(path, title, desc, body, extra_js=""):
    nav = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == path else ""
        cls = ' class="nav-cta"' if label == "Wholesale" else ""
        nav.append(f'<li><a href="{href}"{cls}{cur}>{label}</a></li>')
    full_title = "Pun Labs: novelty gifts, office and art supplies" if path == "/" else f"{title} | Pun Labs"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Pun Labs">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#7A489C">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&family=Montserrat:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
<div class="wrap head-in">
<a class="brand" href="/"><img src="/assets/punlabs-logo.svg" alt="Pun Labs" width="168" height="30"></a>
<nav aria-label="Main"><ul class="nav">{''.join(nav)}</ul></nav>
</div>
</header>
<main id="main">
{body}
</main>
<footer class="site-foot">
<div class="wrap">
<div class="foot-grid">
<div>
<img src="/assets/punlabs-logo.svg" alt="Pun Labs" width="140" height="25">
<p>Pun Labs LLC makes novelty gifts, office and art supplies in Charlotte, North Carolina. Practically punny.</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div>
<div>
<h2>Pun Labs</h2>
<ul><li><a href="/brands/">Brands</a></li><li><a href="/wholesale/">Wholesale</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li><li><a href="/assets/grant-weatherford.vcf" download>Save contact card</a></li></ul>
</div>
<div>
<h2>Buy Pop Colors</h2>
<ul><li><a href="{LINKS['shop']}">popcolors.com</a></li><li><a href="{LINKS['amazon']}">Amazon</a></li><li><a href="{LINKS['etsy']}">Etsy</a></li><li><a href="{LINKS['faire']}">Faire (for retailers)</a></li></ul>
</div>
</div>
<p class="parent small">Pun Labs is a <a href="{LINKS['ubc']}">Universal Benefit Corporation</a> company. &copy; <span data-year>2026</span> Pun Labs LLC.</p>
</div>
</footer>
<script>document.querySelectorAll("[data-year]").forEach(function(e){{e.textContent=new Date().getFullYear()}});</script>
{extra_js}
</body>
</html>
'''


def product_grid(items, four=False):
    lis = []
    for name, kind, handle, img in items:
        src = CDN + img + "&width=600"
        lis.append(f'''<li class="product"><a href="{LINKS['shop']}/products/{handle}">
<div class="ph"><img src="{src}" alt="{html.escape(name)} by Pop Colors" width="600" height="600" loading="lazy"></div>
<h3>{html.escape(name)}</h3><p>{html.escape(kind)}</p></a></li>''')
    return f'<ul class="products{" four" if four else ""}">' + "".join(lis) + "</ul>"


def channels():
    rows = [
        ("Pop Colors store", "Our own shop, with every set and bundle.", LINKS["shop"], "Visit popcolors.com"),
        ("Amazon", "Pop Colors sets from the Pun Labs store.", LINKS["amazon"], "Shop on Amazon"),
        ("Etsy", "The PopColorsCo shop.", LINKS["etsy"], "Shop on Etsy"),
        ("Faire", "Wholesale for independent retailers.", LINKS["faire"], "Order on Faire"),
    ]
    return '<ul class="channels">' + "".join(
        f'<li class="channel"><a href="{u}"><strong>{t}</strong><span>{d}</span><span class="go">{g}</span></a></li>'
        for t, d, u, g in rows) + "</ul>"


HERO_PENCILS = "".join(pencil(t, PENCIL_COLORS[i], l) for i, (t, l) in enumerate([
    ("PUN LABS", 100), ("PRACTICALLY PUNNY", 86), ("NOVELTY GIFTS", 94),
    ("OFFICE SUPPLIES", 80), ("ART SUPPLIES", 90), ("POP COLORS", 76)]))

YELLOW = ("#F2C230", "#F7D460", "#D4A514")
SERIOUS_LINES = ["SERIOUS SUPPLY. FOR WRITING, NOT FUN.", "SERIOUS SUPPLY. MANDATORY EFFORT.",
                 "SERIOUS SUPPLY. PLEASE DO NOT SMILE.", "SERIOUS SUPPLY. ATTEND THE MEETING."]
SERIOUS_PENCILS = "".join(pencil(t, YELLOW, 100, tone="ink", font="Courier Prime", base=430) for t in SERIOUS_LINES)

def graphite_pencil(label, body, light, dark, ink, parts, shape="hex", uid="g"):
    """A graphite office pencil with eraser and ferrule, pointing right, imprint along the barrel.
    parts: list of (x, kind, value) where kind is 'text' or 'bubbles' (value = count)."""
    w, top, h = 560, 6, 40
    bx = w - 66
    if shape == "round":
        fill = f'url(#{uid})'
        defs = (f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1">'
                f'<stop offset="0" stop-color="{dark}"/><stop offset=".28" stop-color="{light}"/>'
                f'<stop offset=".55" stop-color="{body}"/><stop offset="1" stop-color="{dark}"/></linearGradient></defs>')
        facets = ""
    else:
        fill, defs = body, ""
        facets = (f'<rect x="64" y="{top}" width="{bx-64}" height="12" fill="{light}"/>'
                  f'<rect x="64" y="{top+h-12}" width="{bx-64}" height="12" fill="{dark}"/>')
    imprint = []
    for x, kind, val in parts:
        if kind == "text":
            imprint.append(f'<text x="{x}" y="{top+h/2+5}" font-family="Courier Prime, monospace" font-size="13" font-weight="700" fill="{ink}">{html.escape(val)}</text>')
        else:
            for i in range(val):
                imprint.append(f'<circle cx="{x + i*15}" cy="{top+h/2}" r="5" fill="none" stroke="{ink}" stroke-width="1.6"/>')
    return f'''<svg class="gpencil" viewBox="0 0 {w} 52" role="img" aria-label="{html.escape(label)}">{defs}
<rect x="0" y="{top+2}" width="30" height="{h-4}" rx="5" fill="#E8A5A2"/>
<rect x="26" y="{top}" width="38" height="{h}" fill="#C7CBD1"/>
<rect x="26" y="{top}" width="38" height="8" fill="#E2E5E9"/>
<rect x="34" y="{top}" width="3" height="{h}" fill="#9EA4AC"/><rect x="53" y="{top}" width="3" height="{h}" fill="#9EA4AC"/>
<rect x="64" y="{top}" width="{bx-64}" height="{h}" fill="{fill}"/>{facets}
<polygon points="{bx},{top} {w-20},{top+h/2-5} {w-20},{top+h/2+5} {bx},{top+h}" fill="#E9C9A0"/>
<polygon points="{bx},{top} {w-20},{top+h/2-5} {w-20},{top+h/2-1} {bx},{top+12}" fill="#F2D9B6"/>
<polygon points="{w-20},{top+h/2-5} {w},{top+h/2} {w-20},{top+h/2+5}" fill="#3B3B3D"/>
{''.join(imprint)}
</svg>'''


FIRST_DESIGNS = [
    ("7901 Pencil-Supervisor", "Royal blue, round, with foil lettering. Stupendous graphite.",
     graphite_pencil("7901 Pencil-Supervisor pencil", "#2346A8", "#4A6FD0", "#152C73", "#E6C76A",
                     [(84, "text", "SERIOUS SUPPLY CO."), (262, "text", "7901 PENCIL-SUPERVISOR"),
                      ], shape="round", uid="gp1")),
    ("Test Slaying 101", "Black, round, with answer-sheet bubbles.",
     graphite_pencil("Test Slaying 101 pencil", "#1E1E20", "#4A4A4E", "#0A0A0B", "#F1F1F1",
                     [(84, "text", "TEST SLAYING 101"), (240, "bubbles", 5), (322, "text", "SERIOUS SUPPLY CO.")],
                     shape="round", uid="gp2")),
    ("601 Good News", "Silver, hexagonal, plain graphite.",
     graphite_pencil("601 Good News pencil", "#B9BEC5", "#D8DCE1", "#959BA3", "#1B1B1B",
                     [(84, "text", "601 SERIOUS SUPPLY CO. GOOD NEWS"), (352, "text", "CHARLOTTE, N.C.")],
                     shape="hex", uid="gp3")),
]

FIRST_DESIGNS_HTML = ('<div class="wrap designs"><h3>First designs</h3><p class="typed">Three graphite pencils, now in development.</p><ul class="design-list">'
                      + "".join(f'<li>{svg}<p><strong>{html.escape(n)}</strong><br>{html.escape(d)}</p></li>' for n, d, svg in FIRST_DESIGNS)
                      + '</ul></div>')

PNEUMART_SECTION = '''<section class="pneumart" id="pneumart" aria-labelledby="pa-h">
<div class="wrap">
<span class="soon">Coming soon</span>
<h2 id="pa-h" class="pa-word">Pneum<span>ART</span></h2>
<p class="pa-tag">The spirit of Art lives here.</p>
<p>A new art supply line from Pun Labs.</p>
<p>Want to hear when it launches? <a href="/contact/?topic=pneumart">Ask to be told</a>.</p>
</div>
</section>'''

SERIOUS_SECTION = f'''<section class="serious" id="serious-supply" aria-labelledby="ss-h">
<div class="wrap split">
<div>
<span class="soon">Coming soon</span>
<h2 id="ss-h">Serious Supply</h2>
<div class="memo"><p>Memo: a new line of office supplies from Pun Labs.</p><p>Plain pencils. Stern instructions.</p><p>Please hold all laughter until further notice.</p></div>
<p class="typed" style="margin-top:22px">Want to know when it ships? <a href="/contact/?topic=serious">Ask to be told</a>.</p>
</div>
<div class="pencils" aria-label="Serious Supply pencil imprints">{SERIOUS_PENCILS}</div>
</div>
{FIRST_DESIGNS_HTML}
</section>'''


def home():
    body = f'''<section class="hero">
<div class="wrap hero-grid">
<div>
<span class="tag">Practically punny</span>
<h1>Novelty gifts, office and art supplies.</h1>
<p class="lede">Pun Labs makes Pop Colors: colored pencil sets where every pencil is foil-stamped with a pun or reference tied to its color, drawn from the shows, films, music, games and artists people love.</p>
<div class="btns"><a class="btn" href="/wholesale/">Wholesale</a><a class="btn ghost" href="{LINKS['shop']}">Shop Pop Colors</a></div>
</div>
<div class="pencils" aria-hidden="true">{HERO_PENCILS}</div>
</div>
</section>
<section class="band" aria-labelledby="pc-h">
<div class="wrap">
<div class="section-head">
<h2 id="pc-h">From the Pop Colors line</h2>
<p>Pencil sets, coloring pages and bundles that pair the two. A few of the current sets:</p>
</div>
{product_grid(PRODUCTS[:6])}
<div class="btns"><a class="btn ghost" href="/brands/">More about our brands</a></div>
</div>
</section>
<section aria-labelledby="buy-h">
<div class="wrap">
<div class="section-head"><h2 id="buy-h">Where to buy</h2><p>Shoppers can buy Pop Colors online. Retailers can order wholesale on Faire or directly from us.</p></div>
{channels()}
</div>
</section>
<section class="strip" aria-labelledby="ws-h">
<div class="wrap">
<h2 id="ws-h">Stocking a store?</h2>
<p class="lede">Independent shops can order Pop Colors on Faire. For direct accounts, larger volumes, corporate gifts or custom work, tell us what you need.</p>
<div class="btns"><a class="btn" href="/wholesale/">Wholesale options</a><a class="btn ghost" href="{LINKS['faire']}">Order on Faire</a></div>
</div>
</section>'''
    return page("/", "Home", "Pun Labs LLC is a novelty gift, office and art supply company in Charlotte, NC, and the maker of Pop Colors colored pencil sets.", body)


def brands():
    body = f'''<div class="page-head"><div class="wrap"><h1>Our brands</h1><p class="lede">Pun Labs is the company behind Pop Colors, with new office and art lines on the way.</p></div></div>
<section aria-labelledby="pop-h" style="padding-top:32px">
<div class="wrap">
<div class="split">
<div>
<img class="brand-mark" src="/assets/popcolors-logo.svg" alt="Pop Colors" width="260" height="32">
<h2 id="pop-h" class="skip">Pop Colors</h2>
<p class="lede">Pop Colors celebrates pop culture and nostalgia, one pencil at a time.</p>
<p>Each set holds 12 pre-sharpened hexagonal colored pencils, and each pencil is foil-stamped with a pun or reference tied to its color. Sets are themed around favorite TV shows, films, music, video games and painters. Many come with coloring pages printed on heavy cardstock, sold on their own or bundled with the pencils.</p>
<div class="btns"><a class="btn" href="{LINKS['shop']}">Shop popcolors.com</a><a class="btn ghost" href="/wholesale/">Carry Pop Colors</a></div>
</div>
<div>
<h3>What's in the line</h3>
<ul class="facts">
<li>Colored pencil sets of 12</li>
<li>Coloring page packs</li>
<li>Pencil and coloring page bundles</li>
<li>Themes for TV, film, music, games, art and kids</li>
</ul>
<p class="small muted">Sold at popcolors.com, on Amazon and Etsy, and wholesale through Faire.</p>
</div>
</div>
<div style="margin-top:48px">{product_grid(PRODUCTS, four=True)}</div>
</div>
</section>
{SERIOUS_SECTION}
{PNEUMART_SECTION}'''
    return page("/brands/", "Our brands", "Pop Colors colored pencil sets and coloring pages, plus Serious Supply and PneumART, new office and art lines coming soon from Pun Labs.", body)


def wholesale():
    body = f'''<div class="page-head"><div class="wrap"><h1>Wholesale</h1><p class="lede">Pop Colors suits gift shops, bookstores, art supply and museum stores, and corporate gifting. Here's how to order.</p></div></div>
<section style="padding-top:32px" aria-label="Ways to order">
<div class="wrap">
<div class="ways">
<div class="way"><h3>Order on Faire</h3><p>Independent retailers can browse the full Pop Colors range and order through our Faire shop.</p><a class="btn" href="{LINKS['faire']}">Open our Faire shop</a></div>
<div class="way"><h3>Order directly, in volume or custom</h3><p>For direct accounts, chains and big-box buyers, corporate gifts, or custom and private-label work, send an inquiry below and we'll follow up by email.</p><a class="btn ghost" href="#inquiry">Send an inquiry</a></div>
</div>
</div>
</section>
<section class="band" id="inquiry" aria-labelledby="inq-h">
<div class="wrap">
<div class="section-head"><h2 id="inq-h">Wholesale inquiry</h2><p>Tell us a little about your store and how you'd like to buy.</p></div>
<div class="form-card">{wholesale_form()}</div>
</div>
</section>
<section aria-labelledby="ws-prod-h">
<div class="wrap">
<div class="section-head"><h2 id="ws-prod-h">Popular sets</h2><p>A few current sets. See every product on <a href="{LINKS['faire']}">Faire</a> or <a href="{LINKS['shop']}">popcolors.com</a>.</p></div>
{product_grid(PRODUCTS[:4], four=True)}
</div>
</section>'''
    return page("/wholesale/", "Wholesale", "Order Pop Colors wholesale on Faire, or contact Pun Labs for direct, volume, corporate gift and custom orders.", body, FORM_JS)


def about():
    body = f'''<div class="page-head"><div class="wrap"><h1>About Pun Labs</h1></div></div>
<section style="padding-top:16px" aria-label="Our story">
<div class="wrap split">
<div>
<p class="lede">Pun Labs is a novelty gift, office and art supply company. It makes Pop Colors, a line of colored pencil sets that turn a favorite show, film, band or painter into a box of 12 punny pencils.</p>
<p>The business was already established when its current owner took it on, with Pop Colors sold through its own store, Amazon, Etsy and independent retailers. Today Pun Labs works out of a studio in Charlotte, North Carolina, where it designs new sets and is developing Serious Supply, its first office line.</p>
<p>Pun Labs is part of <a href="{LINKS['ubc']}">Universal Benefit Corporation</a>.</p>
</div>
<div>
<h2>Team</h2>
<div class="person"><div class="initials" aria-hidden="true">GW</div><div><h3 style="margin:4px 0 4px">Grant Weatherford</h3><p class="muted" style="margin-bottom:6px">Runs Pun Labs</p><p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="/assets/grant-weatherford.vcf" download>Save contact card</a></p></div></div>
</div>
</div>
</section>
<section class="band" aria-labelledby="partner-h">
<div class="wrap"><h2 id="partner-h">Partners and press</h2><p>For partnerships, licensing conversations or press, <a href="/contact/?topic=partner">get in touch</a>.</p></div>
</section>'''
    return page("/about/", "About", "About Pun Labs LLC, the Charlotte, NC company behind Pop Colors.", body)


def contact():
    body = f'''<div class="page-head"><div class="wrap"><h1>Contact</h1><p class="lede">Write to us about wholesale, gifting, partnerships, press or anything else. For wholesale, the <a href="/wholesale/#inquiry">wholesale inquiry</a> asks the questions we'll need.</p></div></div>
<section style="padding-top:24px" aria-label="Contact form">
<div class="wrap split">
<div class="form-card">{contact_form()}</div>
<div>
<h2>Other ways to reach us</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Pun Labs LLC<br>Charlotte, North Carolina</p>
<p><a href="/assets/grant-weatherford.vcf" download>Save Grant's contact card</a></p>
</div>
</div>
</section>'''
    return page("/contact/", "Contact", "Contact Pun Labs about wholesale, corporate gifting, partnerships or press.", body, FORM_JS)


def thanks():
    body = f'''<section class="hero"><div class="wrap" style="max-width:760px">
<h1>Thanks. We've got it.</h1>
<p class="lede" id="thanks-msg">Your message reached Pun Labs. We'll reply by email.</p>
<div class="btns"><a class="btn" href="/">Back to the home page</a><a class="btn ghost" href="{LINKS['shop']}">Shop Pop Colors</a></div>
</div></section>
<script>try{{if(new URLSearchParams(location.search).get("f")==="wholesale")document.getElementById("thanks-msg").textContent="Your wholesale inquiry reached Pun Labs. We'll reply by email. If you buy on Faire, you can also order there any time.";}}catch(e){{}}</script>'''
    out = page("/thanks/", "Thanks", "Your message reached Pun Labs.", body)
    return out.replace('<head>\n', '<head>\n<meta name="robots" content="noindex">\n', 1)


def notfound():
    body = '''<section class="hero"><div class="wrap" style="max-width:760px"><h1>That page isn't here.</h1><p class="lede">The link may be old or mistyped.</p><div class="btns"><a class="btn" href="/">Go to the home page</a><a class="btn ghost" href="/contact/">Contact us</a></div></div></section>'''
    return page("/404.html", "Page not found", "Page not found.", body)


def write(rel, text):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(text)


write("index.html", home())
write("brands/index.html", brands())
write("wholesale/index.html", wholesale())
write("about/index.html", about())
write("contact/index.html", contact())
write("thanks/index.html", thanks())
write("404.html", notfound())
write("assets/site.css", CSS.strip() + "\n")
write("assets/favicon.svg", FAVICON)
write("CNAME", "punlabs.io\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
urls = ["/", "/brands/", "/wholesale/", "/about/", "/contact/"]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + "".join(f"<url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
write("assets/grant-weatherford.vcf", "BEGIN:VCARD\r\nVERSION:3.0\r\nN:Weatherford;Grant;;;\r\nFN:Grant Weatherford\r\n"
      "ORG:Pun Labs LLC\r\nEMAIL;TYPE=INTERNET,WORK:" + EMAIL + "\r\nURL:https://punlabs.io\r\n"
      "ADR;TYPE=WORK:;;;Charlotte;NC;;USA\r\nEND:VCARD\r\n")
print("built")
