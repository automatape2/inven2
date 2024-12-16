# download html file from url array and save it to a file

import requests
import os

urls = [
    "https://annual.inven2.com/2023/en/a-word-from-the-ceo/",
    "https://annual.inven2.com/2023/en/innovation-how-do-you-take-your-research-to-market/",
    "https://annual.inven2.com/2023/en/clinical-trials/",
    "https://annual.inven2.com/2023/en/featured_item/attracting-virtual-clinical-trials-to-norway/",
    "https://annual.inven2.com/2023/en/featured_item/analysing-samples-from-paediatric-oncology-patients-throughout-europe/",
    "https://annual.inven2.com/2023/en/featured_item/clinical-studies-important-for-norwegian-companies/",
    "https://www.inven2.com/about-us/board-of-directors/",
    "https://annual.inven2.com/2023/en/featured_item/vaccibody-2/",
    "https://annual.inven2.com/2023/en/featured_item/zelluna/",
    "https://annual.inven2.com/2023/en/featured_item/epiguard-2/",

    "https://annual.inven2.com/2023/en/featured_item/probnp/",
    "https://annual.inven2.com/2023/en/featured_item/medical-thermo-band-2/",
    "https://annual.inven2.com/2023/en/featured_item/promon-shield-2/",
    "https://annual.inven2.com/2023/en/featured_item/inner-beauty-2/",
    "https://annual.inven2.com/2023/en/featured_item/epishuttle-2/",
    "https://annual.inven2.com/2023/en/featured_item/multi-needle-langmuir-probe-m-nlp/",
    "https://annual.inven2.com/2023/en/ecosystem/",
]

for url in urls:
    r = requests.get(url)
    archivo = url.split("/")[-2]

    with open("./2023/" + archivo + ".html", "wb") as f:
        f.write(r.content)
    
    print(archivo)


