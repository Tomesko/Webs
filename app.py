import streamlit as st
import streamlit.components.v1 as components

# 1. Nastavení stránky Streamlitu
st.set_page_config(layout="wide", page_title="Pozemek Středokluky | Radomil Hrabě")

# 2. Skrytí výchozího designu Streamlitu (okraje, hlavička, patička)
st.markdown("""
    <style>
        .block-container { 
            padding-top: 0rem !important; 
            padding-bottom: 0rem !important; 
            padding-left: 0rem !important; 
            padding-right: 0rem !important; 
            max-width: 100% !important; 
        }
        header { display: none !important; }
        footer { display: none !important; }
        iframe { border: none; display: block; }
    </style>
""", unsafe_allow_html=True)

# 3. Kompletní HTML kód stránky
html_code = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Exkluzivní stavební pozemek 1378 m² ve Středoklukách. Projekt domu v ceně.">
    <title>Pozemek Středokluky | Radomil Hrabě</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">

    <style>
        /* --- BAREVNÁ PALETA --- */
        :root {
            --primary-green: #1a4d2e;
            --accent-gold: #c6a87c;
            --bg-light: #f4f7f5;
            --text-dark: #2c3531;
            --white: #ffffff;
            --sidebar-width: 280px;
            --shadow-soft: 0 10px 30px rgba(0,0,0,0.08);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        html { scroll-behavior: smooth; }

        body {
            font-family: 'Open Sans', sans-serif;
            background-color: var(--bg-light);
            color: var(--text-dark);
            display: flex;
            min-height: 100vh;
            line-height: 1.7;
        }

        h1, h2, h3, .brand {
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            color: var(--primary-green);
        }

        /* --- SKRYTÉ PRVKY PRO MOBILNÍ MENU --- */
        #menu-toggle { display: none; }
        .menu-toggle-btn { display: none; }
        .overlay { display: none; }

        /* --- LEVÝ PANEL (PC) --- */
        nav.sidebar {
            width: var(--sidebar-width);
            background: linear-gradient(180deg, var(--primary-green) 0%, #143d24 100%);
            height: 100vh;
            position: fixed;
            top: 0; left: 0;
            display: flex; flex-direction: column;
            padding: 3rem 2rem;
            color: var(--white);
            box-shadow: 5px 0 20px rgba(0,0,0,0.15);
            z-index: 2000;
        }

        .brand {
            font-size: 1.8rem; text-transform: uppercase; letter-spacing: 2px;
            margin-bottom: 3rem; color: var(--white);
            border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 1rem;
        }
        .brand span { display: block; font-size: 0.8rem; font-weight: 400; color: var(--accent-gold); margin-top: 5px; letter-spacing: 4px; }

        .nav-links { list-style: none; flex-grow: 1; }
        .nav-links li { margin-bottom: 1rem; }
        .nav-links a {
            text-decoration: none; color: rgba(255,255,255,0.7); font-size: 1rem;
            font-weight: 600; transition: 0.3s; display: flex; align-items: center; padding: 10px 0;
        }
        .nav-links a:hover { color: var(--white); transform: translateX(8px); }
        .nav-links a::before {
            content: ''; display: inline-block; width: 6px; height: 6px;
            background: var(--accent-gold); border-radius: 50%; margin-right: 10px;
            opacity: 0; transition: 0.3s;
        }
        .nav-links a:hover::before { opacity: 1; }

        .contact-mini {
            background: rgba(255,255,255,0.05); backdrop-filter: blur(5px);
            padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); margin-top: auto;
        }
        .contact-mini h4 { color: var(--accent-gold); font-size: 0.7rem; text-transform: uppercase; margin-bottom: 5px; letter-spacing: 1px; }
        .contact-mini p { color: #eee; font-size: 0.9rem; margin-bottom: 2px; font-weight: 600; }
        .contact-mini small { color: #aaa; font-size: 0.8rem; }

        /* --- HLAVNÍ OBSAH --- */
        main.content {
            margin-left: var(--sidebar-width); width: calc(100% - var(--sidebar-width)); padding: 0;
        }

        header.hero {
            /* Místo 'pozemek-hero.jpg' dej svou fotku, až ji budeš mít */
            background: linear-gradient(rgba(26, 77, 46, 0.85), rgba(26, 77, 46, 0.6)), url('pozemek-hero.jpg');
            background-size: cover; background-position: center; background-color: #1a4d2e;
            color: white; min-height: 80vh; display: flex; flex-direction: column; justify-content: center;
            padding: 4rem 6rem;
        }
        header.hero h1 { color: white; font-size: 3.5rem; line-height: 1.1; margin-bottom: 1.5rem; max-width: 800px; }
        header.hero p.lead { font-size: 1.3rem; max-width: 600px; margin-bottom: 2.5rem; font-weight: 300; opacity: 0.9; }

        .btn {
            display: inline-block; background-color: var(--accent-gold); color: #1a1a1a; padding: 16px 40px;
            font-weight: 700; text-decoration: none; border-radius: 50px; text-transform: uppercase;
            letter-spacing: 1px; font-size: 0.9rem; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(198, 168, 124, 0.4);
        }
        .btn:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(198, 168, 124, 0.6); background-color: white; }

        section { padding: 6rem; border-bottom: 1px solid #e0e0e0; }
        section h2 { font-size: 2.2rem; margin-bottom: 2rem; position: relative; display: inline-block; }
        section h2::after { content: ''; position: absolute; bottom: -10px; left: 0; width: 40%; height: 4px; background: var(--accent-gold); border-radius: 2px; }

        .hero-stats {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 30px;
            margin-top: -80px; padding: 0 6rem; position: relative; z-index: 10;
        }
        .stat-box {
            background: white; padding: 2.5rem 2rem; border-radius: 15px; box-shadow: var(--shadow-soft);
            text-align: center; transition: transform 0.3s; border-bottom: 4px solid var(--primary-green);
        }
        .stat-box:hover { transform: translateY(-10px); }
        .stat-box h3 { color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 10px; font-family: 'Open Sans', sans-serif; }
        .stat-box span { font-size: 1.8rem; font-weight: 700; color: var(--primary-green); display: block; }

        .project-card { background: white; border-radius: 20px; overflow: hidden; box-shadow: var(--shadow-soft); display: flex; margin-top: 2rem; }
        .project-info { padding: 3rem; flex: 1; }
        .project-visual { flex: 1; background: #ddd; min-height: 300px; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #777; }

        .gallery-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
        .gallery-item { height: 400px; border-radius: 15px; overflow: hidden; position: relative; cursor: pointer; box-shadow: var(--shadow-soft); background: #eee; }
        .gallery-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; display: block; }
        .gallery-item:hover img { transform: scale(1.05); }
        .gallery-label { position: absolute; bottom: 20px; left: 20px; background: white; padding: 8px 16px; border-radius: 30px; font-weight: 700; font-size: 0.8rem; color: var(--primary-green); box-shadow: 0 4px 10px rgba(0,0,0,0.2); }

        ul.features-list { list-style: none; margin-top: 20px; }
        ul.features-list li { background: white; margin-bottom: 10px; padding: 15px 20px; border-radius: 8px; border-left: 4px solid var(--accent-gold); box-shadow: 0 2px 5px rgba(0,0,0,0.05); display: flex; align-items: center; }
        ul.features-list li strong { color: var(--primary-green); margin-right: 10px; }

        /* =========================================
           MOBILNÍ VERZE - VÝSUVNÉ MENU ZLEVA
           ========================================= */
        @media (max-width: 900px) {
            body { flex-direction: column; }
            
            /* Tlačítko pro otevření menu (hamburger) */
            .menu-toggle-btn {
                display: block; position: fixed; top: 15px; left: 15px;
                background-color: var(--primary-green); color: white;
                padding: 10px 15px; border-radius: 8px; z-index: 2001;
                cursor: pointer; font-weight: bold; font-family: 'Montserrat', sans-serif;
                box-shadow: 0 4px 10px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.2);
            }

            /* Boční panel se schová doleva mimo obrazovku */
            nav.sidebar {
                width: 280px; left: -300px; /* Skryto */
                transition: left 0.4s ease;
                padding-top: 5rem;
            }

            /* Vyjetí panelu */
            #menu-toggle:checked ~ nav.sidebar { left: 0; }

            /* Ztmavení zbytku obrazovky */
            #menu-toggle:checked ~ .overlay {
                display: block; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0,0,0,0.6); z-index: 1999; cursor: pointer;
            }

            main.content { margin-left: 0; width: 100%; }

            .nav-links { display: block; overflow-x: visible; }
            .nav-links li { margin-bottom: 1.5rem; }
            .nav-links a { font-size: 1.1rem; padding: 0; background: transparent; border: none; white-space: normal; }
            .nav-links a:active { background: transparent; color: var(--accent-gold); }
            
            .contact-mini { display: block; margin-top: 2rem; }

            /* Design obsahu pro mobil */
            header.hero { padding: 6rem 1.5rem 4rem 1.5rem; text-align: center; min-height: 50vh; align-items: center; }
            header.hero h1 { font-size: 2.2rem; }
            .hero-stats { margin-top: -30px; padding: 0 1.5rem; grid-template-columns: 1fr 1fr; gap: 15px; position: relative; z-index: 10; }
            .stat-box { padding: 1.5rem 1rem; }
            .stat-box h3 { font-size: 0.7rem; }
            .stat-box span { font-size: 1.4rem; }
            section { padding: 3rem 1.5rem; }
            .project-card { flex-direction: column; }
            .project-info { padding: 2rem 1.5rem; }
            .project-visual { min-height: 200px; }
            .gallery-grid { grid-template-columns: 1fr; gap: 15px; }
            .gallery-item { height: 250px; }
        }
    </style>
</head>
<body>

    <input type="checkbox" id="menu-toggle">
    <label for="menu-toggle" class="menu-toggle-btn">☰ MENU</label>
    <label for="menu-toggle" class="overlay"></label>

    <nav class="sidebar">
        <div class="brand">
            Pod Sedličkami <span>STŘEDOKLUKY</span>
        </div>

        <ul class="nav-links">
            <li><a href="#uvod">Přehled</a></li>
            <li><a href="#projekt">Projekt v ceně</a></li>
            <li><a href="#lokalita">Lokalita</a></li>
            <li><a href="#technicke">Inženýrské sítě</a></li>
            <li><a href="#galerie">Galerie</a></li>
            <li><a href="#kontakt">Kontakt</a></li>
        </ul>

        <div class="contact-mini">
            <h4>Váš makléř</h4>
            <p>Radomil Hrabě</p>
            <small>Výhradní zastoupení</small>
            <p style="margin-top: 5px; color: var(--accent-gold);">+420 603 306 035</p>
        </div>
    </nav>

    <main class="content">

        <header id="uvod" class="hero">
            <h1>Stavební pozemek 1 378 m²<br>s projektem domu</h1>
            <p class="lead">Exkluzivní nabídka ve Středoklukách. Klid, soukromí a připravenost k výstavbě.</p>
            <div>
                <a href="#kontakt" class="btn">Sjednat prohlídku</a>
            </div>
        </header>

        <div class="hero-stats">
            <div class="stat-box">
                <h3>Plocha</h3>
                <span>1 378 m²</span>
            </div>
            <div class="stat-box">
                <h3>Cena</h3>
                <span>6 990 000 Kč</span>
            </div>
            <div class="stat-box">
                <h3>Bonus</h3>
                <span>Projekt RD</span>
            </div>
            <div class="stat-box">
                <h3>Sítě</h3>
                <span>Kompletní</span>
            </div>
        </div>

        <section id="projekt">
            <h2>Projekt domu v ceně</h2>
            <p>Neztrácejte čas papírováním. Součástí prodeje je exkluzivní projekt moderního rodinného domu 5+kk, který je navržen přímo pro tuto parcelu.</p>

            <div class="project-card">
                <div class="project-info">
                    <h3 style="color: var(--primary-green);">Rodinný dům 5+kk</h3>
                    <p>Promyšlená dispozice pro rodinný život. Obývací pokoj propojený se zahradou, 4 neprůchozí ložnice a dostatek úložných prostor.</p>
                    <ul class="features-list">
                        <li><strong>125 m²</strong> Užitná plocha</li>
                        <li><strong>2x</strong> Koupelna + WC</li>
                        <li><strong>Připraveno</strong> K podání na úřad</li>
                    </ul>
                </div>
                <div class="project-visual">
                    <div style="text-align:center; padding: 20px;">
                        VIZUALIZACE PROJEKTU<br>
                        <small>(Vyžádejte si u makléře)</small>
                    </div>
                </div>
            </div>
        </section>

        <section id="lokalita">
            <h2>Středokluky: Žádaná adresa</h2>
            <p>Kombinace absolutního klidu na okraji obce a perfektní dostupnosti do hlavního města.</p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; margin-top: 30px;">
                <div>
                    <h3>🚗 Dostupnost</h3>
                    <ul class="features-list">
                        <li><strong>8-10 min</strong> Praha 6 (Ruzyně, OC Šestka)</li>
                        <li><strong>5-7 min</strong> Letiště Václava Havla</li>
                        <li><strong>20 min</strong> Praha Dejvice (rychlé napojení na dálnici D7)</li>
                    </ul>
                </div>
                <div>
                    <h3>🚌 Hromadná doprava</h3>
                    <ul class="features-list">
                        <li><strong>Linka 322</strong> Přímé spojení na metro A (Veleslavín)</li>
                        <li><strong>Linka 319</strong> Přímé spojení na letiště</li>
                        <li><strong>Linka 324</strong> Směr Praha Zličín nebo Kladno</li>
                    </ul>
                </div>
                <div>
                    <h3>🏫 Vybavenost</h3>
                    <ul class="features-list">
                        <li><strong>Škola</strong> MŠ i ZŠ přímo v obci</li>
                        <li><strong>Služby</strong> Obchod (COOP), Pošta, Veterinární ordinace</li>
                        <li><strong>Relax</strong> Koupaliště, cyklostezky, dětská hřiště</li>
                    </ul>
                </div>
            </div>

            <div style="margin-top: 30px; border-radius: 15px; overflow: hidden; box-shadow: var(--shadow-soft);">
                <div style="background: #eee; height: 350px; display: flex; align-items: center; justify-content: center; color: #777;">
                    <iframe style="border:none;" src="https://mapy.cz/s/purogafotu" width="100%" height="350" frameborder="0"></iframe>
                </div>
            </div>
        </section>

        <section id="technicke" style="background: white;">
            <h2>Inženýrské sítě</h2>
            <p>Pozemek je plně zasíťovaný ("plug & play"). Všechny přípojky jsou na hranici pozemku nebo v přilehlé komunikaci.</p>
            <div class="hero-stats" style="margin-top: 20px; padding: 0;">
                <div class="stat-box" style="border-bottom-color: var(--accent-gold);">
                    <h3>Elektřina</h3>
                    <span>230/400V</span>
                </div>
                <div class="stat-box" style="border-bottom-color: var(--accent-gold);">
                    <h3>Voda</h3>
                    <span>Veřejná</span>
                </div>
                <div class="stat-box" style="border-bottom-color: var(--accent-gold);">
                    <h3>Kanalizace</h3>
                    <span>Veřejná</span>
                </div>
                <div class="stat-box" style="border-bottom-color: var(--accent-gold);">
                    <h3>Plyn</h3>
                    <span>Na hranici</span>
                </div>
            </div>
        </section>

        <section id="galerie">
            <h2>Fotogalerie</h2>
            <div class="gallery-grid">
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 1</div><div class="gallery-label">Vizualizace domu</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 2</div><div class="gallery-label">Pohled na pozemek</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 3</div><div class="gallery-label">Zahrada</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 4</div><div class="gallery-label">Interiér - Obývací pokoj</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 5</div><div class="gallery-label">Interiér - Kuchyně</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 6</div><div class="gallery-label">Interiér - Ložnice</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 7</div><div class="gallery-label">Koupelna</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 8</div><div class="gallery-label">Půdorys 1.NP</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 9</div><div class="gallery-label">Půdorys 2.NP</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 10</div><div class="gallery-label">Okolí pozemku</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 11</div><div class="gallery-label">Příjezdová cesta</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 12</div><div class="gallery-label">Pohled z ulice</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 13</div><div class="gallery-label">Letecký pohled</div></div>
                <div class="gallery-item"><div style="background:#eee; height:100%; display:flex; align-items:center; justify-content:center; color:#777; font-weight:bold;">FOTO 14</div><div class="gallery-label">Detail pozemku</div></div>
            </div>
        </section>

        <section id="kontakt" style="background-color: var(--primary-green); color: white; text-align: center;">
            <h2 style="color: white;">Zaujala vás nabídka?</h2>
            <p style="color: rgba(255,255,255,0.8); max-width: 600px; margin: 0 auto 30px auto;">
                Tento pozemek je skvělou investicí do budoucnosti. Rád vám vše ukážu osobně.
            </p>

            <div style="background: white; padding: 40px; border-radius: 20px; display: inline-block; color: var(--text-dark); box-shadow: 0 20px 50px rgba(0,0,0,0.2); max-width: 500px; width: 100%;">

                <div style="width: 100px; height: 100px; background: #eee; border-radius: 50%; margin: 0 auto 20px auto; overflow: hidden; border: 3px solid var(--accent-gold);">
                    <img src="makler.jpg" alt="Radomil Hrabě" style="width: 100%; height: 100%; object-fit: cover;">
                </div>

                <h3 style="color: var(--primary-green); margin-bottom: 5px;">Radomil Hrabě</h3>
                <p style="margin-bottom: 5px; font-weight: 600;">Soukromý makléř</p>
                <p style="margin-bottom: 20px; font-size: 0.9rem; color: #666;">Výhradní zastoupení</p>

                <a href="tel:+420603306035" class="btn" style="width: 100%;">📞 +420 603 306 035</a>
                <a href="mailto:info@pozemek.cz" style="display: block; margin-top: 15px; color: #555; text-decoration: underline;">Napsat e-mail</a>
            </div>
        </section>

    </main>

    <script>
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                // 1. Zabránit Streamlitu v refreshování stránky
                e.preventDefault(); 
                
                // 2. Získat cíl odkazu (např. "#kontakt") a najít ho na stránce
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    // 3. Plynulý odjezd na dané místo
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }

                // 4. Pokud jsme na mobilu a vyjelo menu, tak ho po kliknutí zavřeme
                const menuToggle = document.getElementById('menu-toggle');
                if (menuToggle && menuToggle.checked) {
                    menuToggle.checked = false;
                }
            });
        });
    </script>

</body>
</html>
"""

# 4. Vykreslení kódu. Výška zajišťuje scrollovatelné okno uvnitř Streamlitu.
components.html(html_code, height=1000, scrolling=True)
