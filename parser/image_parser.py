import json
from urllib.request import urlretrieve
import time
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data = """


{
    "products": [
      {
        "costDeft": "",
        "name": "TP-LINK TL-SF1008P \u043a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "tp-link-tl-sf1008p-kommutator-switch",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "43.9$",
        "cost": "460 950",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7009/240_59817408e1ba7.jpg",
        "id": 7009,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK TL-SG1008P \u041a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "tp-link-tl-sg1008p-kommutator-switch",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "61.4$",
        "cost": "644 700",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7010/240_5981767570b14.jpg",
        "id": 7010,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK TL-SG1008PE \u041a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "tp-link-tl-sg1008pe-kommutator-switch",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "126.8$",
        "cost": "1 331 400",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7011/240_5981775864095.jpg",
        "id": 7011,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK T1600G-28PS \u041a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "tp-link-t1600g-28ps-kommutator-switch",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "322$",
        "cost": "3 381 000",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7013/240_59817b2498157.jpg",
        "id": 7013,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK TL-R860 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0438\u0437\u0430\u0442\u043e\u0440 (router)",
        "SEO_name": "tp-link-tl-r860-marshrutizator-router",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "29.2$",
        "cost": "306 600",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7014/240_59818a40677df.jpg",
        "id": 7014,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK TL-R470T+ \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0438\u0437\u0430\u0442\u043e\u0440 (router)",
        "SEO_name": "tp-link-tl-r470t-marshrutizator-router",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "43.4$",
        "cost": "455 700",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7015/240_59818d29e8a5f.jpg",
        "id": 7015,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK TL-SL1226 \u043a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "tp-link-tl-sl1226-kommutator-switch",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "77$",
        "cost": "808 500",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7016/240_59818e981b025.jpg",
        "id": 7016,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK TL-SL2428 \u043a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "tp-link-tl-sl2428-kommutator-switch",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "127.8$",
        "cost": "1 341 900",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7017/240_5981903ef20fd.jpg",
        "id": 7017,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK JetStream T2500G-10TS \u043a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "tp-link-jetstream-t2500g-10ts-kommutator-switch",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "108.3$",
        "cost": "1 137 150",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7018/240_598191cc3f23a.jpg",
        "id": 7018,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK TL-SG5412F \u043a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440",
        "SEO_name": "tp-link-tl-sg5412f-kommutator",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "229.3$",
        "cost": "2 407 650",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7019/240_59819472beadf.jpg",
        "id": 7019,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK T2600G-18TS (TL-SG3216)",
        "SEO_name": "tp-link-t2600g-18ts-tl-sg3216",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "184.4$",
        "cost": "1 936 200",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7020/240_5981a2fed01f7.jpg",
        "id": 7020,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "TP-LINK TL-SL5428E \u043a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "tp-link-tl-sl5428e-kommutator-switch",
        "brand": "TP-LINK",
        "favorite": 0,
        "sale": "",
        "costDollar": "219.5$",
        "cost": "2 304 750",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7021/240_5981a4db84312.jpg",
        "id": 7021,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "D-link DES-3200-52 \u043a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "d-link-des-3200-52-kommutator-switch",
        "brand": "D-link",
        "favorite": 0,
        "sale": "",
        "costDollar": "525$",
        "cost": "5 512 500",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7022/240_5981a8c6bad1b.jpg",
        "id": 7022,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "D-link DGS-3000-10TC \u043a\u043e\u043c\u043c\u0443\u0442\u0430\u0442\u043e\u0440 (switch)",
        "SEO_name": "d-link-dgs-3000-10tc-kommutator-switch",
        "brand": "D-link",
        "favorite": 0,
        "sale": "",
        "costDollar": "272.27$",
        "cost": "2 858 835",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7023/240_5981aa17e709e.jpg",
        "id": 7023,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "D-link DAP-1350 Wi-Fi-\u0440\u043e\u0443\u0442\u0435\u0440",
        "SEO_name": "d-link-dap-1350-wi-fi-router",
        "brand": "D-link",
        "favorite": 0,
        "sale": "",
        "costDollar": "55$",
        "cost": "577 500",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7025/240_5982df4a69412.jpg",
        "id": 7025,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "D-link DAP-1360 Wi-Fi-\u0440\u043e\u0443\u0442\u0435\u0440",
        "SEO_name": "d-link-dap-1360-wi-fi-router",
        "brand": "D-link",
        "favorite": 0,
        "sale": "",
        "costDollar": "39.03$",
        "cost": "409 815",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7026/240_5982e3ac34f73.jpg",
        "id": 7026,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "D-Link DWA-525/EU \u0431\u0435\u0441\u043f\u0440\u043e\u0432\u043e\u0434\u043d\u043e\u0439 \u0430\u0434\u0430\u043f\u0442\u0435\u0440",
        "SEO_name": "d-link-dwa-525-eu-besprovodnoy-adapter",
        "brand": "D-link",
        "favorite": 0,
        "sale": "",
        "costDollar": "14.63$",
        "cost": "153 615",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7027/240_5982e6ec32a69.jpg",
        "id": 7027,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "VoIP \u0448\u043b\u044e\u0437, VoIP GATEWAY GXW4004 FXS",
        "SEO_name": "voip-shlyuz-voip-gateway-gxw4004-fxs",
        "brand": "Grandstream",
        "favorite": 0,
        "sale": "",
        "costDollar": "138$",
        "cost": "1 449 000",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7112/240_598852191530a.jpg",
        "id": 7112,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "VoIP \u0448\u043b\u044e\u0437, VoIP GATEWAY GXW4104 FXO",
        "SEO_name": "voip-shlyuz-voip-gateway-gxw4104-fxo",
        "brand": "Grandstream",
        "favorite": 0,
        "sale": "",
        "costDollar": "217$",
        "cost": "2 278 500",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7116/240_598941a040a3b.jpg",
        "id": 7116,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "VoIP \u0448\u043b\u044e\u0437, VoIP GATEWAY GXW4224",
        "SEO_name": "voip-shlyuz-voip-gateway-gxw4224",
        "brand": "Grandstream",
        "favorite": 0,
        "sale": "",
        "costDollar": "533$",
        "cost": "5 596 500",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7118/240_598979a0969e8.jpg",
        "id": 7118,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "Grandstream HT503 \u0430\u0434\u0430\u043f\u0442\u0435\u0440 \u0434\u043b\u044f VoIP-\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u0438",
        "SEO_name": "grandstream-ht503-adapter-dlya-voip-telefonii",
        "brand": "Grandstream",
        "favorite": 0,
        "sale": "",
        "costDollar": "61$",
        "cost": "640 500",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7119/240_59897f9b1e412.jpg",
        "id": 7119,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "\u041f\u0430\u0442\u0447 \u043f\u0430\u043d\u0435\u043b\u044c \u043e\u043f\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043d\u0435\u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u0430\u044f 1U",
        "SEO_name": "patch-panel-opticheskaya-nezagruzhennaya-1u",
        "brand": "FortPro",
        "favorite": 0,
        "sale": "",
        "costDollar": "26$",
        "cost": "273 000",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7353/240_5b5ea1cf4600b.jpg",
        "id": 7353,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "\u041f\u0430\u0442\u0447 \u043f\u0430\u043d\u0435\u043b\u044c \u043e\u043f\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043d\u0435\u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u0430\u044f 2U",
        "SEO_name": "patch-panel-opticheskaya-nezagruzhennaya-2u",
        "brand": "FortPro",
        "favorite": 0,
        "sale": "",
        "costDollar": "45$",
        "cost": "472 500",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7354/240_5b5ea2f6857d8.jpg",
        "id": 7354,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "\u041c\u0435\u0442\u0430\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043d\u0430\u0441\u0442\u0435\u043d\u043d\u044b\u0439 \u0431\u043e\u043a\u0441 (\u043f\u0430\u0442\u0447 \u043f\u0430\u043d\u0435\u043b\u044c) 32 \u043f\u043e\u0440\u0442\u0430",
        "SEO_name": "metalicheskiy-nastennyy-boks-patch-panel-32-porta",
        "brand": "FortPro",
        "favorite": 0,
        "sale": "",
        "costDollar": "40$",
        "cost": "420 000",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7355/240_599bb7a6eb618.jpg",
        "id": 7355,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "\u041c\u0438\u043a\u0440\u043e-\u0431\u043e\u043a\u0441 \u043e\u043f\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441 \u043f\u043b\u0430\u043d\u043a\u043e\u0439 \u043f\u043e\u0434 \u0430\u0434\u0430\u043f\u0442\u043e\u0440\u044b",
        "SEO_name": "mikro-boks-opticheskiy-s-plankoy-pod-adaptory",
        "brand": "FortPro",
        "favorite": 0,
        "sale": "",
        "costDollar": "5.5$",
        "cost": "57 750",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7358/240_599bbc2dd6ac7.jpg",
        "id": 7358,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "\u0410\u0434\u0430\u043f\u0442\u0435\u0440 SC/APC, SM, Simplex, Adapter SC/APC",
        "SEO_name": "adapter-sc-apc-sm-simplex-adapter-sc-apc",
        "brand": "FortPro",
        "favorite": 0,
        "sale": "",
        "costDollar": "0.63$",
        "cost": "6 615",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7361/240_599c09aae1d22.jpg",
        "id": 7361,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "\u0410\u0434\u0430\u043f\u0442\u0435\u0440 LC/UPC, SM, Duplex, Adapter LC/UPC",
        "SEO_name": "adapter-lc-upc-sm-duplex-adapter-lc-upc",
        "brand": "FortPro",
        "favorite": 0,
        "sale": "",
        "costDollar": "1.42$",
        "cost": "14 910",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7362/240_599c0b59c12d5.jpg",
        "id": 7362,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "\u0410\u0434\u0430\u043f\u0442\u0435\u0440 SC/UPC, SM, Simplex, Adapter SC/UPC",
        "SEO_name": "adapter-sc-upc-sm-simplex-adapter-sc-upc",
        "brand": "FortPro",
        "favorite": 0,
        "sale": "",
        "costDollar": "0.63$",
        "cost": "6 615",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7363/240_599c0c7e4fd3c.jpg",
        "id": 7363,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "\u0410\u0434\u0430\u043f\u0442\u0435\u0440 FC/UPC SM D-\u0442\u0438\u043f\u0430",
        "SEO_name": "adapter-fc-upc-sm-d-tipa",
        "brand": "FortPro",
        "favorite": 0,
        "sale": "",
        "costDollar": "0.82$",
        "cost": "8 610",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7364/240_599c0d90c1ef3.jpg",
        "id": 7364,
        "qty_rev": 0
      },
      {
        "costDeft": "",
        "name": "\u0410\u0434\u0430\u043f\u0442\u0435\u0440 SC/UPC, \u041cM, Simplex, Adapter SC/UPC",
        "SEO_name": "adapter-sc-upc-mm-simplex-adapter-sc-upc",
        "brand": "FortPro",
        "favorite": 0,
        "sale": "",
        "costDollar": "0.82$",
        "cost": "8 610",
        "costOld": "",
        "stars": 0,
        "main_img": "https://my.abad.uz/images/119/7365/240_599c10301210b.jpg",
        "id": 7365,
        "qty_rev": 0
      }
    ],
    "pcat_id": "2",
    "cat_id": "121",
    "success": true
  }
"""


def read_files():
    files = os.listdir(os.path.join(ROOT_DIR, 'media'))
    return files


if __name__ == '__main__':
    start = time.time()
    json_file = open('./parsed_data/abad_products.json', 'r')
    json_datas = json.load(json_file)
    files = read_files()
    for json_data in json_datas:
        products = json_data['products']
        for product in products:
            if product['main_img']:
                img_src = product['main_img']
                file_name = str(img_src).split('/')[-1]
                if files not in files:
                    load_media = urlretrieve(img_src, './media/{}'.format(file_name))
    end = time.time()
    print(end - start)
