import csv
import pandas as pd
import mysql.connector

#name = pd.read_csv('product_data_csv',['name'])










product_csv = [{'name': 'Milton Antibacterial Surface Wipes x30', 'price': '£2.75', 'price_per': '£2.75 / ea', 'nectar_price': '£2.05', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/milton-antibacterial-surface-wipes-x30'},
{'name': 'Napisan Powder 800g', 'price': '£4.50', 'price_per': '£4.50 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/napisan-powder-800g'},
{'name': 'Milton Sterilising Fluid 1L', 'price': '£4.00', 'price_per': '£4.00 / ea', 'nectar_price': '£3.00', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/milton-sterilising-fluid-1l'},
{'name': 'Milton Sterilising Tablets x28', 'price': '£2.75', 'price_per': '10p / ea', 'nectar_price': '£2.05', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/milton-sterilising-tablets-x28'},
{'name': "Sainsbury's Little Ones Bottle & Teat Cleaning Brush", 'price': '£2.80', 'price_per': '£2.80 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-bottle-teat-cleaning-brush'},      
{'name': 'Lansinoh Disposable Breast Pads Pack of 60', 'price': '£6.50', 'price_per': '11p / ea', 'nectar_price': '£5.20', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/lansinoh-disposable-breast-pads-x60'},
{'name': 'Tommee Tippee Softly Scented Citrus Refills x3', 'price': '£16.00', 'price_per': '£5.33 / ea', 'nectar_price': '£14.00', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommee-tippee-softly-scented-citrus-refills-x3'},
{'name': "Johnson's Baby Honey Soap Duo Pack 2x90g", 'price': '£1.00', 'price_per': '£1.11 / 100g', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/johnsons-baby-honey-soap-duo-pack-2x90g'},
{'name': "Sainsbury's Disposable Breast Pads x40", 'price': '£1.80', 'price_per': '5p / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-disposable-breast-pads-x40'},
{'name': 'Tommee Tippee Closer to Nature Fast Flow Teats 6m+ x2', 'price': '£5.50', 'price_per': '£5.50 / ea', 'nectar_price': '£4.00', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommee-tippee-closer-to-nature-fast-flow-teats-6m-x2'},
{'name': 'Tommee Tippee First Cup (Colour Varies)', 'price': '£2.10', 'price_per': '£2.10 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommee-tippee-first-cup'},
{'name': 'Munchkin Click Lock Tip & Sip Cup', 'price': '£6.45', 'price_per': '£6.45 / ea', 'nectar_price': '£5.50', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/munchkin-click-lock-tip---sip-cup'},
{'name': 'Tommee Tippee Closer to Nature Night Time x2 Orthodontic Soo...', 'price': '£5.60', 'price_per': '£2.80 / ea', 'nectar_price': '£4.00', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommee-tippee-closer-to-nature-night-time-x2-orthodontic-soothers-18-36-months'},
{'name': "Sainsbury's Little Ones Catch All Bib 4+ Months", 'price': '£2.60', 'price_per': '£2.60 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-catch-all-bib-4-months'},
{'name': 'Tommee Tippee Brush & Comb', 'price': '£2.50', 'price_per': '£2.50 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommee-tippee-brush---comb'},
{'name': 'MAM Original Pure 16+ Months ', 'price': '£8.30', 'price_per': '£8.30 / ea', 'nectar_price': '£6.20', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/mam-pure-night-16m-soother-2pk'},
{'name': 'Nelsons Teetha Granules x24', 'price': '£5.00', 'price_per': '21p / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/nelson-teetha-granules-x24'},
{'name': "Sainsbury's Little Ones Toddler's Stainless Steel Cutlery 12...", 'price': '£3.00', 'price_per': '£3.00 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-toddlers-stainless-steel-cutlery-12-months'},
{'name': "Sainsbury's Little Ones 5 Feeding Spoons 6+ Months", 'price': '£2.50', 'price_per': '50p / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-5-feeding-spoons-6-months'},
{'name': "Sainsbury's Little Ones Non Spill Cup 6 Months+", 'price': '£2.60', 'price_per': '£2.60 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-non-spill-cup-6-months'},
{'name': 'Braun ThermoScan 3 High Speed Compact Ear Thermometer', 'price': '£37.00', 'price_per': '£12.33 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/braun-thermoscan-3-high-speed-compact-ear-thermometer'},
{'name': 'Tommee Tippee Closer To Nature Night Soother, 6-18 Months x2', 'price': '£5.60', 'price_per': '£2.80 / ea', 'nectar_price': '£4.00', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommee-tippee-closer-to-nature-night-soother-6-18-months-x2'},
{'name': 'Mam Anti-Colic Bottle x2 160ml', 'price': '£18.00', 'price_per': '£9.00 / ea', 'nectar_price': '£13.50', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/mam-anti-colic-bottle-x2-160ml'},
{'name': "Sainsbury's Little Ones Airflow Soothers with Sterilising Ca...", 'price': '£2.80', 'price_per': '£1.40 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-airflow-soothers-with-sterilising-case-6-18-months-x2'},
{'name': "Sainsbury's Little Ones Non Spill Beaker 6 Months+", 'price': '£2.45', 'price_per': '£2.45 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-non-spill-beaker-6-months'},
{'name': 'Mam Fast Flow Teat x2', 'price': '£6.90', 'price_per': '£3.45 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/mam-fast-flow-teat-x2'},
{'name': 'Bathtime Buddies Fun Sponge', 'price': '£1.75', 'price_per': '£1.75 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/bathtime-buddies-fun-sponge'},
{'name': "Sainsbury's Little Ones 2 Standard Neck Silicone Teats Fast ...", 'price': '£1.40', 'price_per': '70p / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-2-standard-neck-silicone-teats-fast-flow-6-months'},
{'name': "Sainsbury's Little Ones Standard Neck Feeding Bottle 0+ Mont...", 'price': '£1.20', 'price_per': '£1.20 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-standard-neck-feeding-bottle-0-months'},
{'name': 'Munchkin 360 Trainer Cup', 'price': '£7.00', 'price_per': '£7.00 / ea', 'nectar_price': '£5.50', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/munchkin-miracle-360-trainer-cup'},
{'name': 'Munchkin Bath Letters And Numbers', 'price': '£8.00', 'price_per': '£8.00 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/munchkin-bath-letters-and-numbers'},
{'name': "Sainsbury's Bowl", 'price': '£1.50', 'price_per': '£1.50 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-bowl'},
{'name': 'Mam Medium Flow Teat 30g x2', 'price': '£6.90', 'price_per': '£3.45 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/mam-medium-flow-teat-30g-x2'},
{'name': 'Mam Easy Active Baby Bottle 4+ Months 330ml', 'price': '£8.50', 'price_per': '£2.83 / 100ml', 'nectar_price': '£6.35', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/mam-easy-active-baby-bottle-4-months-330ml'},
{'name': "Sainsbury's Little Ones 3 Standard Neck Feeding Bottles Slow...", 'price': '£3.25', 'price_per': '£1.08 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-3-standard-neck-feeding-bottles-slow-flow-0-months'},
{'name': "Sainsbury's Little Ones 2 Wide Neck Silicone Teats 6+ Months", 'price': '£1.70', 'price_per': '85p / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-2-wide-neck-silicone-teats-6-months'},
{'name': 'Medela Contact Nipple Shields M 20mm', 'price': '£9.00', 'price_per': '£21.43 / 100g', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/medela-contact-nipple-shields-m-20mm'},
{'name': 'Nuby Chewbies Teethers 3 Months+ Twinpack', 'price': '£4.50', 'price_per': '£2.25 / ea', 'nectar_price': '£3.50', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/nuby-chewbies-teethers-3-months-twinpack'},
{'name': "Sainsbury's Little Ones Milk Powder Dispenser 0+ Months", 'price': '£2.25', 'price_per': '£2.25 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-milk-powder-dispenser-0-months'},
{'name': "Sainsbury's Plate", 'price': '£1.50', 'price_per': '£1.50 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-plate'},
{'name': 'Tommee Tippee Closer To Nature Perfect Preparation Filter', 'price': '£13.50', 'price_per': '£13.50 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tomme-tippee-closer-to-nature-perfect-preparation-filter'},
{'name': 'MAM Start Pure 0-2 Months', 'price': '£6.25', 'price_per': '£3.13 / ea', 'nectar_price': '£5.55', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/mam-pure-start-0-2m-soother-2pk'},
{'name': "Sainsbury's Little Ones Easy Grip Cutlery Set 9+ Months", 'price': '£3.15', 'price_per': '£1.58 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-easy-grip-cutlery-set-9-months'},
{'name': 'MAM Original Pure 6+ Months', 'price': '£7.40', 'price_per': '£7.40 / ea', 'nectar_price': '£5.55', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/mam-pure-original-6m-soother'},
{'name': "Nuby 1st Sipeez Grip n' Sip 4m up to 12 Months+ 240ml", 'price': '£4.25', 'price_per': '£4.25 / ea', 'nectar_price': '£3.50', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/nuby-1st-sipeez-grip-n-sip-4m-up-to-12-months-240ml'},
{'name': 'Tommee Tippee Big Kids 1st Cutlery Set Stainless Steel 12+ M...', 'price': '£5.50', 'price_per': '£5.50 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommee-tippee-big-kids-1st-cutlery-set-stainless-steel-12-months'},
{'name': 'Tommee Tippee Closer to Nature Fun Style x2 Orthodontic Soot...', 'price': '£5.60', 'price_per': '£2.80 / ea', 'nectar_price': '£4.00', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommtctn-fun-soother-18-36-months-x-2'},    
{'name': 'Munchkin Dandy Dots Bath Mat', 'price': '£15.00', 'price_per': '£15.00 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/munchkin-dandy-dots-bath-mat'},
{'name': 'Tommee Tippee Softee Weaning Spoons 4 Months+ x5', 'price': '£3.80', 'price_per': '76p / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommee-tippee-softee-weaning-spoons-4-months-x5'},
{'name': "Sainsbury's Little Ones 2 Wide Neck Feeding Bottles 0+ Month...", 'price': '£3.95', 'price_per': '£1.98 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-2-wide-neck-feeding-bottles-0-months'},
{'name': "Sainsbury's Little Ones Newborn Soothers with Sterilising Ca...", 'price': '£2.75', 'price_per': '£1.38 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-newborn-soothers-with-sterilising-case-0-6-months-x2'},
{'name': "Sainsbury's Little Ones Water Filled Cooler Teether 3+ Month...", 'price': '£1.50', 'price_per': '£1.50 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-water-filled-cooler-teether-3-months'},
{'name': 'Braun ThermoScan Hygiene Cap Ear Thermometer Cover', 'price': '£9.00', 'price_per': '23p / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/braun-thermoscan-hygiene-cap-ear-thermometer-cover'},
{'name': "Sainsbury's Little Ones Day & Night Soothers with Sterilisin...", 'price': '£2.80', 'price_per': '£1.40 / ea', 'nectar_price': None, 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/sainsburys-little-ones-day-night-soothers-with-sterilising-case-6-18-months-x2'},
#{'name': 'Nuby Flip-It Cup', 'price': '£4.25', 'price_per': '£4.25 / ea', 'nectar_price': '£3.50', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/nuby-flip--it-cup'},
{'name': 'Tommee Tippee Closer to Nature 1 Baby Bottle Slow Flow 0m+ 2...', 'price': '£7.50', 'price_per': '£2.88 / 100ml', 'nectar_price': '£6.00', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/tommee-tippee-ctn-1x-260ml-bottle'},     
#{'name': 'Nuby Icy Bite Teether, 3+ Months', 'price': '£6.00', 'price_per': '£6.00 / ea', 'nectar_price': '£4.50', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/nuby-icy-bite-teether--3-months'},
{'name': 'MAM Original Pure 2-6 Months', 'price': '£8.30', 'price_per': '£8.30 / ea', 'nectar_price': '£6.20', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/mam-pure-night-2-6m-soother-2pk'},
#{'name': 'Nuby Thirsty Kids Active Cup Mighty Swig 18+ months 360ml', 'price': '£7.50', 'price_per': '£7.50 / ea', 'nectar_price': '£5.00', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/nuby-thirsty-kids-active-cup-mighty-swig-18-months-360ml'},
{'name': 'Nûby Active Cup Incredible Gulp 18 Months+', 'price': '£7.50', 'price_per': '£7.50 / ea', 'nectar_price': '£5.00', 'price_kg': None, 'product_link': 'https://www.sainsburys.co.uk/gol-ui/product/n%C3%BBby-active-cup-incredible-gulp-18-months'}]



db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1001',
    database = 'testdatabase'
)

mycursor = db.cursor()

#mycursor.execute('CREATE DATABASE testdatabase')


#product = db.cursor()

#mycursor.execute("CREATE TABLE product (name VARCHAR(250), product_link VARCHAR(250) )")

for product_data in product_csv:
    mycursor.execute("INSERT INTO product (name, product_link) VALUES (%(name)s, %(product_link)s)", product_data)

db.commit()