#!/usr/bin/env python3
"""Generate 24 location-specific service pages for PanoptesDrones."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ── Location data ──────────────────────────────────────────────────────
LOCATIONS = {
    'lekki': {
        'name': 'Lekki',
        'slug': 'lekki',
        'geo': '6.4698;3.5852',
        'icbm': '6.4698, 3.5852',
        'loc_page': 'locations/lekki/',
        'sub_areas': 'Banana Island, Lekki Phase 1, Lekki Phase 2, Chevron, Elegushi Beach, Ajah & Abraham Adesanya',
        'real_estate': {
            'hero': 'Drone Photography for Real Estate in Lekki',
            'hero_sub': 'Luxury waterfront estates, Phase 1 villas, and off-plan developments — captured with 4K aerial media that makes buyers act fast.',
            'why_title': 'Lekki Properties Deserve More Than Ground-Level Photos',
            'why_body': 'Lekki is Lagos\'s most dynamic real estate corridor. From Banana Island\'s waterfront mansions to the rapid Lekki-Epe Expressway developments, properties here command premium prices — and buyers expect premium presentation. Aerial media reveals what ground photos hide: full estate footprints, lagoon proximity, rooftop amenities, and neighbourhood context that justifies price tags.',
            'detail_title': 'What aerial media captures in Lekki:',
            'details': [
                '<strong>Banana Island Compounds</strong> — Show private jetties, waterfront gardens, and the exclusivity of island living from above.',
                '<strong>Lekki Phase 1 Estates</strong> — Reveal gated community layouts, road access, and proximity to schools and malls.',
                '<strong>Off-Plan Developments</strong> — Communicate scale and ambition for new projects along Lekki-Epe Expressway.',
                '<strong>Oceanfront Properties</strong> — Capture Atlantic coastline proximity that photographs can\'t convey from the ground.',
                '<strong>Ajah & Abraham Adesanya Growth Corridor</strong> — Document emerging estate developments with contextual aerial overviews.',
            ],
            'who_list': ['Banana Island property agents', 'Phase 1 estate developers', 'Off-plan project marketers', 'Luxury villa consultants', 'PropTech platforms listing Lekki', 'Diaspora property investment firms'],
            'cta_heading': 'Ready to Showcase Lekki Properties?',
            'cta_text': 'Fast scheduling across Lekki. Professional results. Book your next property shoot.',
        },
        'construction': {
            'hero': 'Construction Drone Monitoring in Lekki',
            'hero_sub': 'Track progress on Lekki\'s fast-moving developments — from Phase 1 towers to Free Trade Zone infrastructure — with scheduled aerial documentation.',
            'why_title': 'Lekki\'s Construction Boom Needs Aerial Oversight',
            'why_body': 'Lekki is Lagos\'s most active construction zone. The Lekki-Epe corridor, Free Trade Zone, and Phase 1 tower projects are reshaping the peninsula. Aerial monitoring gives developers, project managers, and investors real-time visibility into site progress without scaffolding or interrupting work crews.',
            'detail_title': 'Construction monitoring in Lekki covers:',
            'details': [
                '<strong>Lekki Free Trade Zone</strong> — Document industrial-scale infrastructure development with periodic flyovers.',
                '<strong>Phase 1 High-Rises</strong> — Track vertical progress on residential towers with consistent comparison shots.',
                '<strong>Chevron Drive Estates</strong> — Monitor gated community builds from foundation to finishing.',
                '<strong>Lekki-Epe Expressway Projects</strong> — Road infrastructure and commercial developments along the corridor.',
                '<strong>Ajah New Estates</strong> — Document phased development across multiple plots for investor updates.',
            ],
            'who_list': ['Property developers in Lekki', 'Project management firms', 'Free Trade Zone contractors', 'Engineering consultancies', 'Estate development companies', 'Infrastructure investors'],
            'cta_heading': 'Track Your Lekki Project From Above',
            'cta_text': 'Scheduled aerial visits. Consistent documentation. Progress your stakeholders can see.',
        },
        'events': {
            'hero': 'Event & Wedding Drone Coverage in Lekki',
            'hero_sub': 'Elegushi Beach weddings, estate venue receptions, and outdoor events — captured with cinematic drone footage that ground cameras can\'t match.',
            'why_title': 'Lekki Events Deserve the Aerial Perspective',
            'why_body': 'Lekki hosts some of Lagos\'s most stunning outdoor events. Beach weddings on Elegushi, lakeside receptions in Phase 1 estates, and Landmark Beach events all share one thing — they\'re designed for spectacle. Aerial footage captures the full scale of these gatherings, creating highlight reels that guests share and couples treasure.',
            'detail_title': 'Event coverage across Lekki:',
            'details': [
                '<strong>Elegushi Beach Weddings</strong> — Sweeping shoreline reveals and ceremony tracking shots along the Atlantic coast.',
                '<strong>Lekki Phase 1 Estate Venues</strong> — Capture the luxury of private compound events with orbiting aerials.',
                '<strong>Landmark Beach Events</strong> — Document corporate and social events against the oceanfront backdrop.',
                '<strong>Lakeside Celebrations</strong> — Lagoon-side venues shine from above, showing water features and ambiance.',
                '<strong>Outdoor Concert & Festival Coverage</strong> — Crowd reveals and atmosphere shots for large-scale gatherings.',
            ],
            'who_list': ['Wedding planners in Lekki', 'Beach event coordinators', 'Estate venue managers', 'Corporate event agencies', 'Couple & family celebrations', 'Social event photographers'],
            'cta_heading': 'Capture Your Lekki Event From Above',
            'cta_text': 'Beach weddings, estate receptions, and outdoor gatherings — book your aerial coverage.',
        },
        'commercial': {
            'hero': 'Commercial Drone Shoots in Lekki',
            'hero_sub': 'Brand campaigns, developer marketing, and corporate content — shot on location across Lekki with cinema-quality aerial production.',
            'why_title': 'Lekki\'s Landscape Is Made for Aerial Storytelling',
            'why_body': 'Lekki\'s coastline, luxury estates, and rapid development make it one of Lagos\'s most visually compelling locations. Whether you\'re a developer marketing a new project, a brand shooting lifestyle content, or a production house filming B-roll, aerial footage from Lekki elevates any production.',
            'detail_title': 'Commercial aerial use cases in Lekki:',
            'details': [
                '<strong>Real Estate Developer Marketing</strong> — Cinematic flyovers for estate launches, investor decks, and sales videos.',
                '<strong>Lifestyle Brand Content</strong> — Oceanfront and luxury estate backdrops for fashion, wellness, and luxury brands.',
                '<strong>Hospitality & Tourism</strong> — Hotel and resort marketing with sweeping coastal aerials.',
                '<strong>Corporate Documentation</strong> — Campus overviews, facility tours, and operational footage for annual reports.',
                '<strong>Social Media Campaigns</strong> — Vertical drone clips optimized for Instagram Reels and TikTok.',
            ],
            'who_list': ['Real estate developers', 'Marketing & ad agencies', 'Lifestyle and fashion brands', 'Hospitality businesses', 'Film & production houses', 'Corporate communications teams'],
            'cta_heading': 'Plan Your Lekki Shoot',
            'cta_text': 'Professional aerial production across Lekki. Tell us your project — we\'ll handle the rest.',
        },
    },
    'victoria-island': {
        'name': 'Victoria Island',
        'slug': 'victoria-island',
        'geo': '6.4281;3.4219',
        'icbm': '6.4281, 3.4219',
        'loc_page': 'locations/victoria-island/',
        'sub_areas': 'Ahmadu Bello Way, Adeola Odeku, Kofo Abayomi, Eko Hotel area, Bar Beach, Oniru',
        'real_estate': {
            'hero': 'Drone Photography for Real Estate on Victoria Island',
            'hero_sub': 'High-rise apartments, ocean-view penthouses, and mixed-use developments — captured with aerial media that commands attention in Lagos\'s business district.',
            'why_title': 'VI Properties Need to Stand Out in a Premium Market',
            'why_body': 'Victoria Island is Lagos\'s prime business and residential hub. Properties here compete for attention from expatriates, corporate executives, and high-net-worth individuals. Aerial media shows what floor plans can\'t: the ocean proximity, skyline views, traffic accessibility, and prestigious address context that drive purchase decisions.',
            'detail_title': 'What aerial media highlights on VI:',
            'details': [
                '<strong>Highrise Apartments</strong> — Show ocean views, rooftop amenities, and building scale relative to the skyline.',
                '<strong>Oniru Private Estates</strong> — Reveal exclusive gated community layouts and beach proximity.',
                '<strong>Mixed-Use Developments</strong> — Capture commercial-residential integration and street-level accessibility.',
                '<strong>Eko Atlantic Adjacency</strong> — Position VI properties relative to the Eko Atlantic mega-project next door.',
                '<strong>Bar Beach Proximity</strong> — Waterfront properties gain enormous visual value from aerial perspectives.',
            ],
            'who_list': ['Luxury apartment agents on VI', 'Expatriate relocation firms', 'Corporate housing providers', 'Mixed-use developers', 'Serviced apartment operators', 'International property consultants'],
            'cta_heading': 'Elevate Your VI Listings',
            'cta_text': 'Premium aerial media for Victoria Island properties. Fast turnaround, professional results.',
        },
        'construction': {
            'hero': 'Construction Drone Monitoring on Victoria Island',
            'hero_sub': 'Track high-rise builds, road infrastructure, and commercial developments across Lagos\'s busiest district with aerial documentation.',
            'why_title': 'VI Construction Needs Consistent Oversight',
            'why_body': 'Victoria Island\'s dense urban environment makes traditional site monitoring challenging. Space is tight, access is restricted, and projects move fast. Aerial monitoring provides complete site visibility without disrupting active work — ideal for high-rise builds along Ahmadu Bello Way and Adeola Odeku.',
            'detail_title': 'Construction monitoring on Victoria Island:',
            'details': [
                '<strong>High-Rise Office Towers</strong> — Track floor-by-floor progress with consistent aerial comparison shots.',
                '<strong>Road & Infrastructure Works</strong> — Document roadworks along Ahmadu Bello Way and Adeola Odeku.',
                '<strong>Commercial Developments</strong> — Monitor retail and office building projects in the business district.',
                '<strong>Hotel & Hospitality Builds</strong> — Track new hotel developments near the Eko Hotel corridor.',
                '<strong>Eko Atlantic Border Projects</strong> — Document developments bridging VI and the Eko Atlantic reclamation.',
            ],
            'who_list': ['Commercial developers on VI', 'Project management consultancies', 'Infrastructure contractors', 'Hotel & hospitality developers', 'Government infrastructure agencies', 'Engineering firms'],
            'cta_heading': 'Monitor Your VI Project',
            'cta_text': 'Scheduled aerial documentation across Victoria Island. Consistent, professional delivery.',
        },
        'events': {
            'hero': 'Event & Wedding Drone Coverage on Victoria Island',
            'hero_sub': 'Corporate galas, rooftop receptions, fashion shows, and embassy events — captured with professional drone footage across Lagos\'s premier event district.',
            'why_title': 'VI Hosts Lagos\'s Most Prestigious Events',
            'why_body': 'Victoria Island is where Lagos celebrates. From Eko Hotel ballrooms to rooftop corporate events, VI venues demand visual content that matches their prestige. Aerial coverage adds scale and cinematic quality that elevates any event highlight reel — especially for outdoor receptions and beachfront gatherings.',
            'detail_title': 'Event coverage across Victoria Island:',
            'details': [
                '<strong>Eko Hotel Galas & Conferences</strong> — Capture the scale of Nigeria\'s premier event venue from above.',
                '<strong>Rooftop Corporate Events</strong> — Skyline-backdrop coverage for product launches and corporate celebrations.',
                '<strong>Fashion Shows & Brand Events</strong> — Dynamic aerial angles for runway shows and brand activations.',
                '<strong>Embassy & Diplomatic Receptions</strong> — Discreet, professional aerial documentation.',
                '<strong>Beachfront Social Events</strong> — Bar Beach and Oniru outdoor events captured with sweeping coastal shots.',
            ],
            'who_list': ['Corporate event planners', 'Hotel event coordinators', 'Fashion & lifestyle brands', 'Diplomatic event organisers', 'Wedding planners (VI venues)', 'Conference organisers'],
            'cta_heading': 'Cover Your VI Event From the Sky',
            'cta_text': 'Corporate, social, or private — book aerial coverage for your Victoria Island event.',
        },
        'commercial': {
            'hero': 'Commercial Drone Shoots on Victoria Island',
            'hero_sub': 'Corporate brand campaigns, fintech marketing, hotel content, and business district aerials — produced on location across Victoria Island.',
            'why_title': 'VI Is Lagos\'s Commercial Content Capital',
            'why_body': 'Victoria Island houses Lagos\'s biggest brands, banks, tech companies, and international businesses. Aerial content from VI communicates corporate scale, urban energy, and premium positioning. Whether it\'s a fintech promo, a hotel marketing video, or a corporate annual report, aerial B-roll from VI adds production value.',
            'detail_title': 'Commercial aerial use cases on VI:',
            'details': [
                '<strong>Corporate Brand Videos</strong> — Aerial establishing shots of HQ buildings and business campuses.',
                '<strong>Fintech & Banking Marketing</strong> — Skyline footage positioning brands within Lagos\'s financial district.',
                '<strong>Hotel & Hospitality Content</strong> — Eko Hotel, luxury boutique hotels, and serviced apartments from above.',
                '<strong>Advertising Campaigns</strong> — Cinematic city aerials for TV commercials and digital campaigns.',
                '<strong>Annual Reports & Investor Content</strong> — Professional facility overviews for corporate communications.',
            ],
            'who_list': ['Banks & financial institutions', 'Tech companies & fintechs', 'Advertising agencies', 'Hotel & hospitality brands', 'Multinational corporations', 'Media & production houses'],
            'cta_heading': 'Plan Your VI Commercial Shoot',
            'cta_text': 'Professional aerial production on Victoria Island. Corporate-grade results, every time.',
        },
    },
    'ikoyi': {
        'name': 'Ikoyi',
        'slug': 'ikoyi',
        'geo': '6.4550;3.4317',
        'icbm': '6.4550, 3.4317',
        'loc_page': 'locations/ikoyi/',
        'sub_areas': 'Old Ikoyi, Parkview Estate, Bourdillon Road, Osborne Road, Gerard Road, Dolphin Estate, Falomo',
        'real_estate': {
            'hero': 'Drone Photography for Real Estate in Ikoyi',
            'hero_sub': 'Diplomat-grade mansions, Bourdillon Road compounds, and Parkview Estate villas — presented with aerial media that matches Ikoyi\'s prestige.',
            'why_title': 'Ikoyi\'s Luxury Market Demands Premium Presentation',
            'why_body': 'Ikoyi is Lagos\'s most exclusive residential district. Properties here are purchased by diplomats, business leaders, and the city\'s wealthiest families. Ground photos don\'t convey the compound scale, mature gardens, lagoon proximity, or neighbourhood exclusivity that drive Ikoyi price tags. Aerial media does.',
            'detail_title': 'Aerial media across Ikoyi:',
            'details': [
                '<strong>Bourdillon Road Compounds</strong> — Lagos\'s most expensive address shown with sweeping estate overviews.',
                '<strong>Parkview Estate Villas</strong> — Gated community layouts, garden footprints, and waterway proximity.',
                '<strong>Old Ikoyi Mansions</strong> — Mature tree-lined streets and heritage properties revealed from above.',
                '<strong>Osborne Road Towers</strong> — New luxury high-rises positioned against the Ikoyi skyline.',
                '<strong>Dolphin Estate Apartments</strong> — Lagoon-adjacent living shown in full waterfront context.',
            ],
            'who_list': ['Luxury estate agents in Ikoyi', 'Diplomatic property managers', 'High-net-worth relocation firms', 'Parkview Estate agents', 'Premium property developers', 'International luxury consultants'],
            'cta_heading': 'Present Ikoyi Properties at Their Best',
            'cta_text': 'Aerial media for Ikoyi\'s most exclusive listings. Discreet, professional, premium.',
        },
        'construction': {
            'hero': 'Construction Drone Monitoring in Ikoyi',
            'hero_sub': 'Track luxury residential towers, estate renovations, and premium developments across Lagos\'s most exclusive district.',
            'why_title': 'Ikoyi Developments Need Precision Documentation',
            'why_body': 'Construction in Ikoyi involves high-value projects with demanding stakeholders — developers, investors, and future residents who expect meticulous oversight. Aerial monitoring provides the visual documentation that quarterly reports and investor updates require, without disrupting the exclusivity of the neighbourhood.',
            'detail_title': 'Construction projects we document in Ikoyi:',
            'details': [
                '<strong>Osborne Road Luxury Towers</strong> — Track multi-storey residential builds with monthly aerial progress shots.',
                '<strong>Parkview Estate Developments</strong> — Monitor new builds and major renovations within the gated estate.',
                '<strong>Bourdillon Road Projects</strong> — Discreet documentation of ultra-premium compound constructions.',
                '<strong>Falomo & Gerard Road Developments</strong> — Commercial and residential projects along key corridors.',
                '<strong>Ikoyi-Lekki Link Bridge Area</strong> — Infrastructure and property developments near the bridge.',
            ],
            'who_list': ['Premium property developers', 'Construction management firms', 'Luxury estate builders', 'Architecture practices', 'Investment fund managers', 'Engineering consultancies'],
            'cta_heading': 'Document Your Ikoyi Build',
            'cta_text': 'Discreet, scheduled aerial documentation for Ikoyi\'s premium construction projects.',
        },
        'events': {
            'hero': 'Event & Wedding Drone Coverage in Ikoyi',
            'hero_sub': 'Private estate weddings, high-society galas, and corporate dinners — captured with aerial footage that matches Ikoyi\'s elegance.',
            'why_title': 'Ikoyi Celebrations Deserve Cinematic Coverage',
            'why_body': 'Ikoyi hosts Lagos\'s most exclusive private events — from Parkview Estate garden weddings to corporate dinners at The Wheatbaker and Four Points. These events are intimate, prestigious, and visually stunning. Aerial coverage adds a dimension that transforms event highlights into cinematic experiences.',
            'detail_title': 'Event coverage across Ikoyi:',
            'details': [
                '<strong>Parkview Estate Weddings</strong> — Garden ceremonies and compound receptions captured with discreet aerial orbits.',
                '<strong>Hotel Galas & Corporate Dinners</strong> — The Wheatbaker, Four Points, and other premium venues from above.',
                '<strong>Private Compound Celebrations</strong> — Birthday milestones, anniversaries, and family gatherings.',
                '<strong>Diplomatic Receptions</strong> — Professional coverage for embassy and consulate events.',
                '<strong>Charity & Fundraising Galas</strong> — Large-scale events at Ikoyi\'s premier social venues.',
            ],
            'who_list': ['High-society wedding planners', 'Luxury hotel event teams', 'Diplomatic event coordinators', 'Private event organisers', 'Corporate entertainment firms', 'Philanthropic event managers'],
            'cta_heading': 'Capture Your Ikoyi Event',
            'cta_text': 'Discreet, elegant aerial coverage for Ikoyi\'s most exclusive events.',
        },
        'commercial': {
            'hero': 'Commercial Drone Shoots in Ikoyi',
            'hero_sub': 'Luxury brand campaigns, fashion editorials, diplomatic media, and premium corporate content — produced on location in Ikoyi.',
            'why_title': 'Ikoyi Sets the Scene for Premium Content',
            'why_body': 'Ikoyi\'s tree-lined streets, waterfront compounds, and architectural elegance provide a backdrop that brands pay a premium to access. Aerial footage from Ikoyi communicates luxury, exclusivity, and sophistication — exactly the positioning that high-end brands, fashion houses, and corporate clients need.',
            'detail_title': 'Commercial aerial use cases in Ikoyi:',
            'details': [
                '<strong>Luxury Brand Campaigns</strong> — Fashion, jewellery, and lifestyle brands shot against Ikoyi\'s iconic estates.',
                '<strong>Fashion Editorials</strong> — Aerial establishing shots for magazine and digital fashion content.',
                '<strong>Corporate Communications</strong> — Board-level video production with premium aerial B-roll.',
                '<strong>Real Estate Developer Marketing</strong> — Cinematic project launches for Ikoyi\'s luxury developments.',
                '<strong>Diplomatic & Government Media</strong> — Professional aerial documentation for official communications.',
            ],
            'who_list': ['Luxury fashion brands', 'Premium real estate developers', 'Corporate communications firms', 'Diplomatic media teams', 'Advertising & creative agencies', 'Film & documentary producers'],
            'cta_heading': 'Plan Your Ikoyi Shoot',
            'cta_text': 'Premium aerial content production in Ikoyi. Discreet, professional, cinema-quality.',
        },
    },
    'ikeja': {
        'name': 'Ikeja',
        'slug': 'ikeja',
        'geo': '6.6018;3.3515',
        'icbm': '6.6018, 3.3515',
        'loc_page': 'locations/ikeja/',
        'sub_areas': 'Ikeja GRA, Allen Avenue, Computer Village, Maryland, Oregun, Alausa, Ojodu Berger, Omole Phase 1 & 2',
        'real_estate': {
            'hero': 'Drone Photography for Real Estate in Ikeja',
            'hero_sub': 'GRA luxury homes, Maryland estates, and Omole Phase developments — captured with 4K aerial media for the Lagos mainland premium market.',
            'why_title': 'Ikeja\'s Residential Market Is Growing Fast',
            'why_body': 'Ikeja GRA and surrounding estates are attracting buyers priced out of the Island market but demanding premium quality. Aerial media shows what makes Ikeja competitive: spacious compounds, tree-lined streets, proximity to the airport, and the calm residential character that families value. These selling points are invisible from ground level.',
            'detail_title': 'Aerial media across Ikeja:',
            'details': [
                '<strong>Ikeja GRA Mansions</strong> — Show spacious compounds, mature gardens, and the neighbourhood\'s low-density character.',
                '<strong>Maryland & Anthony Estates</strong> — Residential complexes and town houses near major expressway junctions.',
                '<strong>Omole Phase 1 & 2</strong> — Gated community layouts and individual home presentations.',
                '<strong>Ojodu Berger Developments</strong> — Document emerging estates and new constructions for early buyers.',
                '<strong>Alausa Government Area</strong> — Corporate housing and diplomatic residences near the seat of government.',
            ],
            'who_list': ['Ikeja GRA property agents', 'Mainland estate developers', 'Corporate relocation companies', 'Family home specialists', 'Diaspora investment agents', 'Residential estate marketers'],
            'cta_heading': 'Showcase Ikeja Properties',
            'cta_text': 'Professional aerial media for Ikeja\'s premium residential market. Fast turnaround.',
        },
        'construction': {
            'hero': 'Construction Drone Monitoring in Ikeja',
            'hero_sub': 'Airport zone projects, government developments, and industrial estate builds — documented with aerial monitoring across Lagos\'s capital district.',
            'why_title': 'Ikeja\'s Development Activity Needs Aerial Oversight',
            'why_body': 'Ikeja is a hub of government, industrial, and residential construction. From Alausa government projects to Oregun industrial developments and GRA luxury builds, the district has diverse construction activity that benefits from consistent aerial documentation. Stakeholders get clear, visual progress updates without site visits.',
            'detail_title': 'Construction monitoring across Ikeja:',
            'details': [
                '<strong>Alausa Government Projects</strong> — Track state government infrastructure and building developments.',
                '<strong>Oregun Industrial Estates</strong> — Monitor warehouse and industrial facility builds.',
                '<strong>Ikeja GRA Residential Builds</strong> — Document luxury home construction in the government reservation area.',
                '<strong>Airport Zone Developments</strong> — Projects near Murtala Muhammed Airport (NCAA clearance handled by us).',
                '<strong>Allen Avenue Commercial Projects</strong> — Track commercial and mixed-use developments along the corridor.',
            ],
            'who_list': ['Government contractors', 'Industrial developers', 'GRA residential builders', 'Airport-adjacent project managers', 'Engineering & consulting firms', 'Infrastructure project teams'],
            'cta_heading': 'Track Your Ikeja Build',
            'cta_text': 'Scheduled aerial monitoring across Ikeja. NCAA airport clearance included where needed.',
        },
        'events': {
            'hero': 'Event & Wedding Drone Coverage in Ikeja',
            'hero_sub': 'GRA venue weddings, government ceremonies, corporate launches, and Mainland celebrations — captured with professional aerial coverage.',
            'why_title': 'Ikeja Events Deserve Professional Coverage',
            'why_body': 'Ikeja hosts a wide range of events — from intimate GRA garden weddings to large corporate launches on Allen Avenue and government ceremonies at Alausa. The district\'s spacious venues and outdoor settings are ideal for aerial coverage that captures the full atmosphere and scale.',
            'detail_title': 'Event coverage across Ikeja:',
            'details': [
                '<strong>GRA Garden Weddings</strong> — Spacious compound ceremonies with lush garden backdrops from above.',
                '<strong>Alausa Government Events</strong> — Official ceremonies and state functions documented aerially.',
                '<strong>Allen Avenue Corporate Launches</strong> — Hotel and venue events along Ikeja\'s commercial strip.',
                '<strong>NECA & Industry Events</strong> — Professional conferences and industry gatherings.',
                '<strong>Outdoor Celebrations</strong> — Birthday milestones and family events in private compounds.',
            ],
            'who_list': ['GRA-based wedding planners', 'Government event coordinators', 'Corporate event agencies', 'Allen Avenue hotel event teams', 'Private celebration organisers', 'Conference & seminar planners'],
            'cta_heading': 'Book Aerial Coverage in Ikeja',
            'cta_text': 'Professional drone coverage for Ikeja events. Government, corporate, or private.',
        },
        'commercial': {
            'hero': 'Commercial Drone Shoots in Ikeja',
            'hero_sub': 'Industrial documentation, government media, tech content, and corporate brand shoots — produced on location across Ikeja.',
            'why_title': 'Ikeja Is Lagos\'s Administrative & Industrial Hub',
            'why_body': 'As Lagos State\'s capital and a major industrial centre, Ikeja is home to government institutions, logistics operations, tech businesses in Computer Village, and corporate headquarters. Aerial content from Ikeja communicates operational scale, institutional credibility, and strategic location.',
            'detail_title': 'Commercial aerial use cases in Ikeja:',
            'details': [
                '<strong>Industrial & Logistics Documentation</strong> — Warehouse complexes and manufacturing facilities from above.',
                '<strong>Government & Institutional Media</strong> — Alausa government precinct aerials for official communications.',
                '<strong>Tech Ecosystem Content</strong> — Computer Village and tech hub documentation.',
                '<strong>Airport-Adjacent Business Parks</strong> — Corporate campus overviews near Murtala Muhammed Airport.',
                '<strong>Corporate Annual Reports</strong> — Professional facility aerials for corporate communications.',
            ],
            'who_list': ['Government communications teams', 'Industrial & logistics companies', 'Tech companies in Ikeja', 'Corporate headquarters', 'Manufacturing businesses', 'Airport-adjacent firms'],
            'cta_heading': 'Plan Your Ikeja Shoot',
            'cta_text': 'Industrial, government, or corporate — professional aerial production in Ikeja.',
        },
    },
    'lagos-island': {
        'name': 'Lagos Island',
        'slug': 'lagos-island',
        'geo': '6.4541;3.3947',
        'icbm': '6.4541, 3.3947',
        'loc_page': 'locations/lagos-island/',
        'sub_areas': 'Broad Street, Marina, Balogun, CMS, Isale Eko, Campos, Onikan, Idumota',
        'real_estate': {
            'hero': 'Drone Photography for Real Estate on Lagos Island',
            'hero_sub': 'Commercial conversions, heritage properties, and prime business-district addresses — captured with aerial media that shows Lagos Island\'s unique potential.',
            'why_title': 'Lagos Island\'s Property Market Is Evolving',
            'why_body': 'Lagos Island is undergoing a transformation — commercial buildings becoming mixed-use, heritage properties attracting investors, and the Marina waterfront gaining renewed interest. Aerial media shows what makes Lagos Island properties unique: waterfront access, historic character, and proximity to Nigeria\'s original financial district.',
            'detail_title': 'Aerial media across Lagos Island:',
            'details': [
                '<strong>Marina Waterfront Properties</strong> — Show Lagos Lagoon proximity and harbour views from above.',
                '<strong>Broad Street Commercial</strong> — Office buildings and commercial spaces in Nigeria\'s historic financial district.',
                '<strong>Heritage & Conversion Properties</strong> — Document character buildings being converted to premium residential.',
                '<strong>CMS & Onikan Developments</strong> — Emerging mixed-use projects near cultural institutions.',
                '<strong>Idumota Commercial Strip</strong> — Document dense commercial corridors and market-adjacent properties.',
            ],
            'who_list': ['Commercial property agents', 'Heritage property investors', 'Mixed-use developers', 'Marina-area agents', 'Legal district property firms', 'Offshore investor representatives'],
            'cta_heading': 'Showcase Lagos Island Properties',
            'cta_text': 'Heritage, commercial, or waterfront — professional aerial media for Lagos Island listings.',
        },
        'construction': {
            'hero': 'Construction Drone Monitoring on Lagos Island',
            'hero_sub': 'Marina redevelopment, infrastructure works, and commercial builds across Lagos\'s oldest business district — tracked with scheduled aerial documentation.',
            'why_title': 'Lagos Island\'s Renewal Needs Visual Progress',
            'why_body': 'Lagos Island is seeing significant infrastructure investment — bridge approaches, marina redevelopment, and commercial building projects that are reshaping the original city centre. Aerial monitoring documents this transformation for developers, government agencies, and investors who need consistent visual progress reports.',
            'detail_title': 'Construction documentation on Lagos Island:',
            'details': [
                '<strong>Marina Redevelopment</strong> — Track waterfront infrastructure and building projects along the Marina.',
                '<strong>Bridge Infrastructure</strong> — Document works on Eko Bridge and Carter Bridge approaches.',
                '<strong>Broad Street Commercial Projects</strong> — Monitor office building renovations and new builds.',
                '<strong>CMS Area Developments</strong> — Track mixed-use and institutional construction projects.',
                '<strong>Market Area Infrastructure</strong> — Document infrastructure improvements around Balogun and Idumota.',
            ],
            'who_list': ['Government infrastructure agencies', 'Commercial developers', 'Bridge and road contractors', 'Urban renewal project teams', 'Heritage building restorers', 'Municipal works departments'],
            'cta_heading': 'Document Your Lagos Island Project',
            'cta_text': 'Aerial monitoring for Lagos Island\'s construction and renewal projects.',
        },
        'events': {
            'hero': 'Event & Wedding Drone Coverage on Lagos Island',
            'hero_sub': 'Eko Hotel functions, Civic Centre events, marina gatherings, and cultural celebrations — captured with aerial footage across Lagos\'s premier event hub.',
            'why_title': 'Lagos Island Is Nigeria\'s Event Capital',
            'why_body': 'Lagos Island hosts more major events per square kilometre than anywhere else in Nigeria. Eko Hotel alone hosts hundreds of events annually, the Civic Centre is a premiere conference destination, and the Marina hosts public celebrations. Aerial coverage adds the cinematic scale these landmark venues deserve.',
            'detail_title': 'Event coverage across Lagos Island:',
            'details': [
                '<strong>Eko Hotel Events</strong> — Nigeria\'s most iconic event venue captured from every aerial angle.',
                '<strong>Civic Centre Conferences</strong> — Corporate and government conferences with scale-showing aerials.',
                '<strong>Marina Public Events</strong> — National celebrations and public gatherings along the waterfront.',
                '<strong>Onikan Cultural Events</strong> — Events at the National Museum and cultural institutions.',
                '<strong>Corporate Award Ceremonies</strong> — Premium indoor-outdoor events at Lagos Island\'s top venues.',
            ],
            'who_list': ['Eko Hotel event coordinators', 'Civic Centre event managers', 'Government event organisers', 'Corporate event agencies', 'Cultural institution events', 'Public celebration organisers'],
            'cta_heading': 'Cover Your Lagos Island Event',
            'cta_text': 'Eko Hotel, Civic Centre, or waterfront — book aerial coverage for your event.',
        },
        'commercial': {
            'hero': 'Commercial Drone Shoots on Lagos Island',
            'hero_sub': 'Financial sector marketing, maritime documentation, historic Lagos media, and corporate content — produced on location across Lagos Island.',
            'why_title': 'Lagos Island Tells a Powerful Visual Story',
            'why_body': 'Lagos Island is where Nigeria\'s financial history meets its commercial present. Broad Street banks, Marina waterfront, Balogun market energy, and institutional landmarks create a visual narrative that serves banking, maritime, government, and corporate clients. Aerial content captures this energy at a scale that ground footage cannot.',
            'detail_title': 'Commercial aerial use cases on Lagos Island:',
            'details': [
                '<strong>Financial Sector Marketing</strong> — Bank headquarters and financial institutions on Broad Street and Marina.',
                '<strong>Maritime & Port Documentation</strong> — Lagos Harbour, port facilities, and shipping operations from above.',
                '<strong>Government & Institutional Content</strong> — Federal and state government facilities and events.',
                '<strong>Historic Lagos Documentaries</strong> — Aerial footage of Lagos Island\'s architectural heritage.',
                '<strong>Market & Commerce Content</strong> — The energy of Balogun, Idumota, and Lagos Island\'s commercial activity.',
            ],
            'who_list': ['Banks & financial institutions', 'Maritime & shipping companies', 'Government media departments', 'Documentary film producers', 'Corporate communications teams', 'Tourism marketing agencies'],
            'cta_heading': 'Plan Your Lagos Island Shoot',
            'cta_text': 'Financial, maritime, or cultural — professional aerial production on Lagos Island.',
        },
    },
    'surulere': {
        'name': 'Surulere',
        'slug': 'surulere',
        'geo': '6.5106;3.3602',
        'icbm': '6.5106, 3.3602',
        'loc_page': 'locations/surulere/',
        'sub_areas': 'Aguda, Itire, Ojuelegba, National Stadium, Adeniran Ogunsanya, Bode Thomas, Eric Moore, Masha',
        'real_estate': {
            'hero': 'Drone Photography for Real Estate in Surulere',
            'hero_sub': 'Affordable estates, mainland family homes, and emerging developments — presented with aerial media that attracts serious buyers to Surulere\'s growing market.',
            'why_title': 'Surulere\'s Market Is Attracting New Attention',
            'why_body': 'Surulere offers what the Island can\'t — spacious homes at accessible prices, a strong community feel, and proximity to the Mainland business district. As buyers get priced out of Lekki and VI, Surulere\'s real estate market is heating up. Aerial media helps listings stand out and shows the neighbourhood context that Surulere buyers care about — schools, worship centres, green spaces, and expressway access.',
            'detail_title': 'Aerial media across Surulere:',
            'details': [
                '<strong>Aguda & Itire Estates</strong> — Family homes and townhouse complexes shown with neighbourhood context.',
                '<strong>National Stadium Vicinity</strong> — Properties near the stadium and National Arts Theatre with landmark proximity.',
                '<strong>Bode Thomas Developments</strong> — New builds and renovated properties along one of Surulere\'s premium streets.',
                '<strong>Adeniran Ogunsanya Corridor</strong> — Mixed-use and residential properties along the commercial strip.',
                '<strong>Eric Moore & Masha</strong> — Estate complexes and apartment buildings with aerial community overviews.',
            ],
            'who_list': ['Mainland estate agents', 'Affordable housing developers', 'First-time buyer specialists', 'Diaspora investment agents', 'Property listing platforms', 'Family home brokers'],
            'cta_heading': 'Showcase Surulere Properties',
            'cta_text': 'Affordable aerial media for Surulere\'s growing real estate market.',
        },
        'construction': {
            'hero': 'Construction Drone Monitoring in Surulere',
            'hero_sub': 'Stadium renovation, residential builds, and commercial developments across Lagos\'s Mainland hub — documented with consistent aerial monitoring.',
            'why_title': 'Surulere Is Being Rebuilt',
            'why_body': 'Surulere is experiencing a construction resurgence — the National Stadium renovation, National Arts Theatre restoration, new residential developments, and commercial projects along key corridors. Aerial monitoring provides the visual accountability that project managers and investors need across multiple active sites.',
            'detail_title': 'Construction monitoring across Surulere:',
            'details': [
                '<strong>National Stadium Renovation</strong> — Track progress on one of Lagos\'s most significant public infrastructure projects.',
                '<strong>National Arts Theatre Restoration</strong> — Document the restoration of a national cultural landmark.',
                '<strong>Residential Developments</strong> — Monitor estate builds in Aguda, Itire, and Eric Moore.',
                '<strong>Adeniran Ogunsanya Commercial</strong> — Track commercial building projects along the retail corridor.',
                '<strong>Bode Thomas & Masha Builds</strong> — New residential and mixed-use developments.',
            ],
            'who_list': ['Government infrastructure contractors', 'Residential developers', 'Public works agencies', 'Renovation project managers', 'Commercial builders', 'Cultural restoration teams'],
            'cta_heading': 'Monitor Your Surulere Project',
            'cta_text': 'Consistent aerial documentation for Surulere construction sites.',
        },
        'events': {
            'hero': 'Event & Wedding Drone Coverage in Surulere',
            'hero_sub': 'National Stadium events, private compound weddings, and community celebrations — captured with aerial footage across Lagos\'s Mainland cultural heart.',
            'why_title': 'Surulere Hosts Lagos\'s Biggest Mainland Events',
            'why_body': 'From National Stadium concerts and sporting events to intimate compound weddings and church celebrations, Surulere is the Mainland\'s event hub. These gatherings are vibrant, colourful, and perfectly suited to aerial coverage that captures the energy and scale that ground cameras miss.',
            'detail_title': 'Event coverage across Surulere:',
            'details': [
                '<strong>National Stadium Events</strong> — Concerts, sports events, and public celebrations from above.',
                '<strong>National Arts Theatre Shows</strong> — Cultural events and performances at the iconic venue.',
                '<strong>Compound Weddings</strong> — Traditional and contemporary ceremonies in private estate settings.',
                '<strong>Church Programmes</strong> — Special services, harvest celebrations, and religious events.',
                '<strong>Community Celebrations</strong> — Street festivals, cultural events, and neighbourhood gatherings.',
            ],
            'who_list': ['Stadium event organisers', 'Mainland wedding planners', 'Church event coordinators', 'Community event organisers', 'Arts & cultural event managers', 'Sports event promoters'],
            'cta_heading': 'Capture Your Surulere Event',
            'cta_text': 'Stadium events, weddings, or community celebrations — book your aerial coverage.',
        },
        'commercial': {
            'hero': 'Commercial Drone Shoots in Surulere',
            'hero_sub': 'Sports media, entertainment content, SME brand shoots, and Mainland commercial documentation — produced on location in Surulere.',
            'why_title': 'Surulere Is Lagos\'s Mainland Content Hub',
            'why_body': 'With the National Stadium, National Arts Theatre, and a thriving SME corridor along Adeniran Ogunsanya, Surulere offers commercial content opportunities that serve sports, entertainment, retail, and emerging brands. Aerial footage adds production value that positions Mainland businesses competitively.',
            'detail_title': 'Commercial aerial use cases in Surulere:',
            'details': [
                '<strong>Sports & Entertainment Media</strong> — National Stadium and National Arts Theatre aerial content.',
                '<strong>SME Brand Content</strong> — Emerging Mainland businesses and retail brands from above.',
                '<strong>Retail Corridor Marketing</strong> — Adeniran Ogunsanya shopping strip aerial documentation.',
                '<strong>Community & Social Enterprise</strong> — NGO and community organisation media production.',
                '<strong>Urban Documentary Content</strong> — Surulere\'s cultural character captured from the air.',
            ],
            'who_list': ['Sports organisations', 'Entertainment companies', 'Mainland SME brands', 'Retail businesses', 'NGOs & social enterprises', 'Documentary & film producers'],
            'cta_heading': 'Plan Your Surulere Shoot',
            'cta_text': 'Sports, entertainment, or commercial — professional aerial production in Surulere.',
        },
    },
}

SERVICES = {
    'real-estate': {
        'tag': 'Real Estate',
        'parent_page': '/real-estate-drone-lagos/',
        'parent_label': 'Real Estate Drone Lagos (All Areas)',
        'section_bg': '#3D4B2F',
        'btn_label': 'Book a Property Shoot',
        'pricing_cards': '''
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Standard Listing</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">From \\u20a655,000</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>60\\u201390 second cinematic aerial video</li>
                        <li>10\\u201315 edited aerial photos</li>
                        <li>48-hour delivery</li>
                        <li>Social media optimized formats</li>
                        <li>Professional operator included</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Book This Package</a>
                    </div>
                </div>
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Bulk Agent Deal</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">Custom Pricing</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>Discounted rate for 5+ properties/month</li>
                        <li>Priority scheduling</li>
                        <li>Consistent style across all listings</li>
                        <li>Dedicated account contact</li>
                        <li>Monthly delivery schedule</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Talk to Us</a>
                    </div>
                </div>''',
    },
    'construction': {
        'tag': 'Construction',
        'parent_page': '/construction-drone-lagos/',
        'parent_label': 'Construction Drone Lagos (All Areas)',
        'section_bg': '#3D4B2F',
        'btn_label': 'Book Site Monitoring',
        'pricing_cards': '''
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Basic</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">From \\u20a635,000/visit</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>Monthly aerial site visit</li>
                        <li>Progress photos (20+ images)</li>
                        <li>Organized digital delivery</li>
                        <li>Professional operator included</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Book This Package</a>
                    </div>
                </div>
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Standard</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">From \\u20a660,000/month</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>2 visits per month</li>
                        <li>Before/after comparison shots</li>
                        <li>Basic site progress report</li>
                        <li>Cloud delivery access</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Book This Package</a>
                    </div>
                </div>
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Pro</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">From \\u20a6100,000/month</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>Weekly aerial visits</li>
                        <li>Full documentation + video</li>
                        <li>Investor-ready progress reports</li>
                        <li>Cloud delivery with archive</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Book This Package</a>
                    </div>
                </div>''',
    },
    'events': {
        'tag': 'Events & Weddings',
        'parent_page': '/events-drone-lagos/',
        'parent_label': 'Event Drone Coverage Lagos (All Areas)',
        'section_bg': '#0E2A47',
        'btn_label': 'Book Event Coverage',
        'pricing_cards': '''
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Event Coverage</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">From \\u20a640,000</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>2\\u20133 hour aerial coverage</li>
                        <li>Crowd reveals & tracking shots</li>
                        <li>72-hour delivery</li>
                        <li>Social media optimized formats</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Book This Package</a>
                    </div>
                </div>
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Wedding Full Day</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">From \\u20a670,000</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>Ceremony + reception coverage</li>
                        <li>Cinematic highlight reel</li>
                        <li>Vertical social media cut</li>
                        <li>48-hour delivery</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Book This Package</a>
                    </div>
                </div>
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Corporate Event</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">Custom Pricing</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>Full-day aerial coverage</li>
                        <li>Multi-angle capture</li>
                        <li>Branded edit available</li>
                        <li>Same-day preview option</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Get a Quote</a>
                    </div>
                </div>''',
    },
    'commercial': {
        'tag': 'Commercial',
        'parent_page': '/commercial-drone-lagos/',
        'parent_label': 'Commercial Drone Lagos (All Areas)',
        'section_bg': '#0E2A47',
        'btn_label': 'Request a Quote',
        'pricing_cards': '''
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Brand / Marketing</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">From \\u20a665,000</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>Half-day aerial shoot</li>
                        <li>4K cinematic B-roll</li>
                        <li>Edited highlight package</li>
                        <li>Social media formats included</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Book This Package</a>
                    </div>
                </div>
                <div class="feature-card" style="background: #111; border: 1px solid rgba(255,255,255,0.2);">
                    <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 0.5rem;">Full Production</h3>
                    <p style="color: var(--color-primary); font-size: 1.6rem; font-weight: 700; margin-bottom: 1rem; letter-spacing: -1px;">Custom Pricing</p>
                    <ul class="use-case-list" style="color: #ffffff;">
                        <li>Full-day aerial production</li>
                        <li>Multi-camera integration</li>
                        <li>Branded edit & colour grade</li>
                        <li>Raw footage delivery option</li>
                    </ul>
                    <div style="text-align: center; margin-top: 1.5rem;">
                        <a href="/contact/" class="btn-hero" style="background: #ffffff; color: #000000;">Get a Quote</a>
                    </div>
                </div>''',
    },
}

SVG_ICONS = {
    'real-estate': '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18M5 21V7l8-4 8 4v14M8 21v-4h8v4"/></svg>',
    'construction': '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 20h20M6 20V10l6-4 6 4v10M10 20v-6h4v6M9 10h6"/></svg>',
    'events': '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/></svg>',
    'commercial': '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
}

CSS_CLASS_MAP = {
    'real-estate': 'real-estate-bg',
    'construction': 'construction-bg',
    'events': 'events-bg',
    'commercial': 'commercial-bg',
}


def build_internal_links(service_key, loc_slug):
    """Build the internal links section HTML."""
    svc = SERVICES[service_key]
    links = []
    # Parent service page
    links.append(f'<li><a href="{svc["parent_page"]}" style="color: var(--color-primary); text-decoration: none;">{svc["parent_label"]}</a></li>')
    # Same service, other locations
    for lk, lv in LOCATIONS.items():
        if lk == loc_slug:
            continue
        fname = f'/{service_key}-drone-{lk}/'
        links.append(f'<li><a href="{fname}" style="color: var(--color-primary); text-decoration: none;">{svc["tag"]} Drone in {lv["name"]}</a></li>')
    # Location general page
    loc = LOCATIONS[loc_slug]
    links.append(f'<li><a href="/{loc["loc_page"]}" style="color: var(--color-primary); text-decoration: none;">All Drone Services in {loc["name"]}</a></li>')
    # Other services for same location
    for sk, sv in SERVICES.items():
        if sk == service_key:
            continue
        fname = f'/{sk}-drone-{loc_slug}/'
        links.append(f'<li><a href="{fname}" style="color: var(--color-primary); text-decoration: none;">{sv["tag"]} Drone in {loc["name"]}</a></li>')
    return '\n                '.join(links)


def generate_page(service_key, loc_slug):
    svc = SERVICES[service_key]
    loc = LOCATIONS[loc_slug]
    data = loc[service_key.replace('-', '_')]
    slug = f'{service_key}-drone-{loc_slug}'
    canonical = f'https://panoptesdrones.com/{slug}/'
    svc_name_loc = f'{svc["tag"]} Drone Services in {loc["name"]}'
    title = f'{data["hero"]} | PanoptesDrones'

    details_html = '\n'.join([f'                                <li>{d}</li>' for d in data['details']])
    who_html = '\n'.join([f'                <li style="display: flex; align-items: center; gap: 0.5rem;"><span style="color: var(--color-primary);">&#10003;</span> {w}</li>' for w in data['who_list']])
    links_html = build_internal_links(service_key, loc_slug)

    airport_note = ''
    if loc_slug == 'ikeja':
        airport_note = '''
    <!-- Airport Notice -->
    <section style="padding: 2rem 0;">
        <div class="container" style="max-width: 800px;">
            <div style="background: #fff3cd; border: 1px solid #ffc107; border-radius: 12px; padding: 1.5rem; text-align: center;">
                <p style="color: #856404; font-weight: 600; margin: 0;">&#9888;&#65039; Ikeja is near Murtala Muhammed International Airport. All drone operations require NCAA airspace clearance. PanoptesDrones handles all permit applications — no extra hassle for you.</p>
            </div>
        </div>
    </section>'''

    html = f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{data['hero_sub'][:160]}">
    <meta name="keywords" content="{service_key.replace('-',' ')} drone {loc['name']}, aerial {svc['tag'].lower()} {loc['name']}, drone {loc['name']}, PanoptesDrones {loc['name']}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="PanoptesDrones">
    <link rel="canonical" href="{canonical}">

    <meta name="geo.region" content="NG-LA">
    <meta name="geo.placename" content="{loc['name']}, Lagos, Nigeria">
    <meta name="geo.position" content="{loc['geo']}">
    <meta name="ICBM" content="{loc['icbm']}">

    <meta property="og:type" content="website">
    <meta property="og:site_name" content="PanoptesDrones">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{data['hero_sub'][:200]}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:locale" content="en_NG">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{data['hero_sub'][:200]}">

    <link rel="stylesheet" href="/styles.css">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "{svc_name_loc}",
        "description": "{data['hero_sub']}",
        "provider": {{
            "@type": "LocalBusiness",
            "name": "PanoptesDrones",
            "url": "https://panoptesdrones.com",
            "telephone": "+2347025580054",
            "address": {{
                "@type": "PostalAddress",
                "streetAddress": "28 Razak Balogun Street, Abule-Oja, Akoka",
                "addressLocality": "Yaba",
                "addressRegion": "Lagos",
                "postalCode": "101283",
                "addressCountry": "NG"
            }}
        }},
        "areaServed": {{
            "@type": "Place",
            "name": "{loc['name']}, Lagos, Nigeria"
        }},
        "serviceType": "Aerial {svc['tag']}"
    }}
    </script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-8MQENQDME0"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-8MQENQDME0');
    </script>
</head>

<body>
    <nav class="navbar">
        <div class="container nav-container">
            <div class="logo">
                <a href="/" style="text-decoration:none;color:inherit;"><img src="/images/panoptesdroneslogo1.png" alt="PanoptesDrones" class="logo-icon"><h1>PanoptesDrones</h1></a>
            </div>
            <ul class="nav-links">
                <li><a href="/about/">About us</a></li>
                <li><a href="/#how-it-works">How it works</a></li>
                <li><a href="/#pricing">Pricing</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/contact/">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <a href="/contact/" class="btn-primary btn-nav">Get a Quote</a>
            </div>
            <a href="/contact/" class="btn-talks-mobile">Let's talk</a>
            <button class="mobile-menu-toggle" id="mobileMenuToggle">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>

    <div class="mobile-menu" id="mobileMenu">
        <ul>
            <li><a href="/about/">About us</a></li>
            <li><a href="/#how-it-works">How it works</a></li>
            <li><a href="/#pricing">Pricing</a></li>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/contact/">Contact</a></li>
            <li><a href="/contact/">Get a Quote</a></li>
        </ul>
    </div>

    <!-- Hero -->
    <section class="about-hero">
        <div class="container">
            <span class="section-tag" style="color: var(--color-primary);">{svc['tag']} &middot; {loc['name']}</span>
            <h1 class="about-hero-title">{data['hero']}</h1>
            <p class="about-hero-subtitle">{data['hero_sub']}</p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 2rem; justify-content: center;">
                <a href="/contact/" class="btn-primary btn-hero">{svc['btn_label']}</a>
                <a href="tel:+2348000000000" class="btn-call">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                    Let's talk
                </a>
            </div>
        </div>
    </section>
{airport_note}
    <!-- Why Section -->
    <section style="padding: 5rem 0;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag">Why It Matters</span>
                <h2 class="section-title">{data['why_title']}</h2>
            </div>
            <div class="feature-rows">
                <div class="feature-row">
                    <div class="feature-text">
                        <h3>{data['why_title']}</h3>
                        <p>{data['why_body']}</p>
                        <div class="feature-detail-container">
                            <h5>{data['detail_title']}</h5>
                            <ul class="use-case-list">
{details_html}
                            </ul>
                        </div>
                    </div>
                    <div class="feature-media {CSS_CLASS_MAP.get(service_key, 'real-estate-bg')}">
                        <div class="feature-media-icon">
                            {SVG_ICONS[service_key]}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Packages -->
    <section id="pricing" style="padding: 5rem 0; background: #000000;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="color: var(--color-primary);">Our Packages</span>
                <h2 class="section-title" style="color: #ffffff;">{svc['tag']} Packages in {loc['name']}</h2>
                <p style="color: #999999; max-width: 600px; margin: 0 auto;">Clear deliverables. Fast turnaround. Every booking includes a professional operator.</p>
            </div>
            <div class="features-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin-top: 3rem; gap: 1.5rem;">
{svc['pricing_cards']}
            </div>
        </div>
    </section>

    <!-- Who We Work With -->
    <section style="padding: 5rem 0; background: {svc['section_bg']};">
        <div class="container" style="text-align: center; max-width: 800px; color: rgba(255,255,255,0.9);">
            <h2 class="section-title" style="color: #ffffff;">Who We Work With in {loc['name']}</h2>
            <p style="color: rgba(255,255,255,0.65); margin-bottom: 2rem;">Professional aerial services for {svc['tag'].lower()} clients across {loc['sub_areas']}.</p>
            <ul style="list-style: none; display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; text-align: left;">
{who_html}
            </ul>
        </div>
    </section>

    <!-- Areas Covered -->
    <section style="padding: 3rem 0; text-align: center;">
        <div class="container">
            <h3 style="margin-bottom: 1rem; font-size: 1.3rem;">Areas We Cover in {loc['name']}</h3>
            <p style="color: var(--color-text-secondary); font-size: 1rem;">{loc['sub_areas']}</p>
        </div>
    </section>

    <!-- Internal Links -->
    <section style="padding: 3rem 0; background: var(--color-bg-secondary);">
        <div class="container" style="max-width: 800px;">
            <h3 style="margin-bottom: 1.5rem; font-size: 1.3rem; text-align: center;">Also Available Across Lagos</h3>
            <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.75rem;">
                {links_html}
            </ul>
        </div>
    </section>

    <!-- CTA -->
    <section style="padding: 5rem 0; background: {svc['section_bg']};">
        <div class="container">
            <div class="about-cta-box" style="background: #ffffff;">
                <h2 style="color: #111111;">{data['cta_heading']}</h2>
                <p style="color: var(--color-text-secondary);">{data['cta_text']}</p>
                <div style="display: flex; justify-content: center; margin-top: var(--spacing-xl);">
                    <a href="/contact/" class="btn-primary btn-hero">{svc['btn_label']}</a>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-column">
                    <h4>PanoptesDrones</h4>
                    <p class="footer-brand-desc">Lagos-based aerial production and inspection company delivering professional drone services for real estate, construction, events, and commercial projects.</p>
                    <div class="footer-contact-line">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                        <span>28 Razak Balogun Street, Abule-Oja, Akoka, Yaba, Lagos 101283</span>
                    </div>
                    <div class="footer-contact-line">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                        <a href="https://wa.me/2347025580054?text=Hello%20I%27d%20like%20to%20make%20an%20enquiry%20about%20your%20drone%20service" target="_blank">070 2558 0054</a>
                    </div>
                    <div class="footer-contact-line">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                        <a href="mailto:micheal@panoptesdrones.com">micheal@panoptesdrones.com</a>
                    </div>
                </div>
                <div class="footer-column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="/real-estate-drone-lagos/">Real Estate Aerial Media</a></li>
                        <li><a href="/construction-drone-lagos/">Construction Monitoring</a></li>
                        <li><a href="/events-drone-lagos/">Event Drone Coverage</a></li>
                        <li><a href="/commercial-drone-lagos/">Commercial Aerial Services</a></li>
                        <li><a href="/drone-rental-lagos/">Drone Rental</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Locations</h4>
                    <ul>
                        <li><a href="/locations/lekki/">Lekki</a></li>
                        <li><a href="/locations/victoria-island/">Victoria Island</a></li>
                        <li><a href="/locations/ikoyi/">Ikoyi</a></li>
                        <li><a href="/locations/ikeja/">Ikeja</a></li>
                        <li><a href="/locations/lagos-island/">Lagos Island</a></li>
                        <li><a href="/locations/surulere/">Surulere</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="/about/">About Us</a></li>
                        <li><a href="/blog/">Blog</a></li>
                        <li><a href="/contact/">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-certs">
                <span>Certified&nbsp;by</span>
                <img src="/images/certs/ncaaimage.webp" alt="Nigerian Civil Aviation Authority (NCAA)" width="120" height="40">
                <img src="/images/certs/cacnigeria.svg" alt="Corporate Affairs Commission Nigeria (CAC)" width="120" height="40">
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 PanoptesDrones. All rights reserved.</p>
                <div class="footer-social">
                    <a href="https://x.com/panoptesdrones" target="_blank" aria-label="X (Twitter)">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </a>
                    <a href="https://instagram.com/panoptesdrones" target="_blank" aria-label="Instagram">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
                    </a>
                    <a href="https://wa.me/2347025580054?text=Hello%20I%27d%20like%20to%20make%20an%20enquiry%20about%20your%20drone%20service" target="_blank" aria-label="WhatsApp">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                    </a>
                </div>
            </div>
        </div>
    </footer>

    <script>
        const mobileMenuToggle = document.getElementById('mobileMenuToggle');
        const mobileMenu = document.getElementById('mobileMenu');
        mobileMenuToggle.addEventListener('click', () => {{
            mobileMenu.classList.toggle('active');
            const spans = mobileMenuToggle.querySelectorAll('span');
            if (mobileMenu.classList.contains('active')) {{
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
            }} else {{
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }}
        }});
    </script>
</body>

</html>
'''
    outdir = os.path.join(ROOT, slug)
    os.makedirs(outdir, exist_ok=True)
    filepath = os.path.join(outdir, 'index.html')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    return slug


# ── Generate all 24 pages ─────────────────────────────────────────────
if __name__ == '__main__':
    created = []
    for svc_key in SERVICES:
        for loc_slug in LOCATIONS:
            fname = generate_page(svc_key, loc_slug)
            created.append(fname)
            print(f'Created: {fname}')

    print(f'\nTotal: {len(created)} pages generated.')
