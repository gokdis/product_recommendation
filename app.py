from flask import Flask, request, jsonify
import pandas as pd

cell_df = pd.DataFrame([{"x":0,"y":0,"sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac"},
             {"x":0,"y":1,"sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac"},
             {"x":0,"y":2,"sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac"},
             {"x":1,"y":0,"sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e"},
             {"x":1,"y":1,"sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e"},
             {"x":1,"y":2,"sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e"},
             {"x":2,"y":0,"sectionId":"1c292782-1120-4498-aedf-873b45b29046"},
             {"x":2,"y":1,"sectionId":"1c292782-1120-4498-aedf-873b45b29046"},
])

position_df = pd.DataFrame([
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d2", "personEmail": "helen@gokdis.ecosys.eu", "x": 0, "y": 0, "time": "2024-04-23 15:30:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d1", "personEmail": "helen@gokdis.ecosys.eu", "x": 0, "y": 2, "time": "2024-04-23 15:40:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d3", "personEmail": "helen@gokdis.ecosys.eu", "x": 2, "y": 0, "time": "2024-04-23 15:50:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d4", "personEmail": "helen@gokdis.ecosys.eu", "x": 1, "y": 2, "time": "2024-04-23 15:55:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d5", "personEmail": "kerberos@gokdis.ecosys.eu", "x": 1, "y": 0, "time": "2024-04-23 15:30:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d6", "personEmail": "kerberos@gokdis.ecosys.eu", "x": 2, "y": 0, "time": "2024-04-23 15:40:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d6", "personEmail": "kerberos@gokdis.ecosys.eu", "x": 2, "y": 0, "time": "2024-04-23 15:50:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d5", "personEmail": "paris@gokdis.ecosys.eu", "x": 0, "y": 1, "time": "2024-04-23 15:50:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d6", "personEmail": "paris@gokdis.ecosys.eu", "x": 2, "y": 0, "time": "2024-04-23 15:55:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d6", "personEmail": "paris@gokdis.ecosys.eu", "x": 2, "y": 0, "time": "2024-04-23 16:00:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d7", "personEmail": "rick@gokdis.ecosys.eu", "x": 0, "y": 0, "time": "2024-04-23 15:30:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d8", "personEmail": "rick@gokdis.ecosys.eu", "x": 0, "y": 0, "time": "2024-04-23 15:45:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d8", "personEmail": "rick@gokdis.ecosys.eu", "x": 0, "y": 0, "time": "2024-04-23 15:55:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e5d9", "personEmail": "jack@gokdis.ecosys.eu", "x": 1, "y": 1, "time": "2024-04-23 15:30:00"},
    {"uid": "7b580377-ca5c-4326-a235-25898711e510", "personEmail": "jack@gokdis.ecosys.eu", "x": 1, "y": 1, "time": "2024-04-23 15:50:00"},
])

section_df = pd.DataFrame([{"id":"2e7e3c54-c5c9-4d99-9c6f-fb38117f3126","name":"canned goods"},
                {"id":"c31db0cc-e796-44b8-8239-6c9a3cc51e95","name":"babies"},
                {"id":"8932701b-9b18-4818-8e7d-d92667a3a59a","name":"dry goods pasta"},
                {"id":"dc41e23f-9919-498e-a894-883640033a05","name":"missing"},
                {"id":"9651a328-c842-4965-8f45-b592a5bd5ddb","name":"produce"},
                {"id":"d1fb5bbc-e358-4039-8ce0-f2f4ef8f328f","name":"household"},
                {"id":"e5650acf-0597-461c-85b8-5679c76df7ac","name":"dairy eggs"},
                {"id":"53cc11d0-4014-42c0-ac0f-42b7e84a9e7a","name":"international"},
                {"id":"dbd8bb0c-95ec-4794-9d14-3618b3698ca1","name":"bulk"},
                {"id":"408ce76e-c6c1-4819-a47a-456627dd7d56","name":"pantry"},
                {"id":"5134cede-8ca7-4e15-ab3d-64362b495d48","name":"deli"},
                {"id":"b516b990-8cd1-4152-9c3f-9049cb14086d","name":"meat seafood"},
                {"id":"63cd2dcd-e1b3-4b53-98c5-dc079db97fcc","name":"breakfast"},
                {"id":"1c292782-1120-4498-aedf-873b45b29046","name":"bakery"},
                {"id":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e","name":"beverages"},
                {"id":"98e916e3-f6da-4e2c-8537-8fc63872512f","name":"frozen"},
                {"id":"2d69e9b6-f927-4732-8a97-93a27691ede8","name":"snacks"},
                {"id":"b312ddc6-7af5-4411-94d1-9ac74d4cefc6","name":"pets"},
                {"id":"4f12f98e-cb83-4231-957b-1ba2a492eedd","name":"alcohol"},
                {"id":"424f7521-4954-40f4-8091-3c1706d30b82","name":"other"},
                {"id":"4816bbae-6670-4253-a47f-e7eac1f32b2b","name":"personal care"}])


order_df = pd.DataFrame([
    {"id":"e9b95f60-49ba-4be6-b565-420a262b840f","personEmail":"helen@gokdis.ecosys.eu","productId":"1b1b3c67-3ae8-47d4-82c0-b0f75ab3a7b5","description":"eggs","quantity":2,"time":"2024-04-23 15:30:00"},
    {"id":"19b95f60-49ba-4be6-b565-420a262b840f","personEmail":"helen@gokdis.ecosys.eu","productId":"2b1c3e36-5299-4744-a0a1-314c3a5d3d43","description":"milk","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"29b95f60-49ba-4be6-b565-420a262b840f","personEmail":"helen@gokdis.ecosys.eu","productId":"904f16e7-92b7-4a97-a0fd-4580843427af","description":"butter","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"39b95f60-49ba-4be6-b565-420a262b840f","personEmail":"paris@gokdis.ecosys.eu","productId":"1b1b3c67-3ae8-47d4-82c0-b0f75ab3a7b5","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"49b95f60-49ba-4be6-b565-420a262b840f","personEmail":"kerberos@gokdis.ecosys.eu","productId":"2b1c3e36-5299-4744-a0a1-314c3a5d3d43","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"59b95f60-49ba-4be6-b565-420a262b840f","personEmail":"kerberos@gokdis.ecosys.eu","productId":"83fbd7b6-6cfb-4c94-ba9a-8b3d79179e84","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"69b95f60-49ba-4be6-b565-420a262b840f","personEmail":"kerberos@gokdis.ecosys.eu","productId":"cc9c8f51-45d8-4fa8-b7c7-dc10e3e3b4a2","description":"","quantity":2,"time":"2024-04-23 15:30:00"},
    {"id":"79b95f60-49ba-4be6-b565-420a262b840f","personEmail":"paris@gokdis.ecosys.eu","productId":"1b1b3c67-3ae8-47d4-82c0-b0f75ab3a7b5","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"89b95f60-49ba-4be6-b565-420a262b840f","personEmail":"paris@gokdis.ecosys.eu","productId":"2b1c3e36-5299-4744-a0a1-314c3a5d3d43","description":"","quantity":2,"time":"2024-04-23 15:30:00"},
    {"id":"99b95f60-49ba-4be6-b565-420a262b840f","personEmail":"paris@gokdis.ecosys.eu","productId":"ce689c97-787a-4793-a587-6a68c5d53cf3","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"10b95f60-49ba-4be6-b565-420a262b840f","personEmail":"jack@gokdis.ecosys.eu","productId":"2b1c3e36-5299-4744-a0a1-314c3a5d3d43","description":"","quantity":2,"time":"2024-04-23 15:30:00"},
    {"id":"11b95f60-49ba-4be6-b565-420a262b840f","personEmail":"rick@gokdis.ecosys.eu","productId":"1b1b3c67-3ae8-47d4-82c0-b0f75ab3a7b5","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"11b95f60-49ba-4be6-b565-420a262b840f","personEmail":"bob@gokdis.ecosys.eu","productId":"1b1b3c67-3ae8-47d4-82c0-b0f75ab3a7b5","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"11b95f60-49ba-4be6-b565-420a262b840f","personEmail":"bob@gokdis.ecosys.eu","productId":"2b1c3e36-5299-4744-a0a1-314c3a5d3d43","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"11b95f60-49ba-4be6-b565-420a262b840f","personEmail":"bob@gokdis.ecosys.eu","productId":"904f16e7-92b7-4a97-a0fd-4580843427af","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"11b95f60-49ba-4be6-b565-420a262b840f","personEmail":"michele@gokdis.ecosys.eu","productId":"1b1b3c67-3ae8-47d4-82c0-b0f75ab3a7b5","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"11b95f60-49ba-4be6-b565-420a262b840f","personEmail":"michele@gokdis.ecosys.eu","productId":"2b1c3e36-5299-4744-a0a1-314c3a5d3d43","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"11b95f60-49ba-4be6-b565-420a262b840f","personEmail":"jackson@gokdis.ecosys.eu","productId":"f1e5d0d0-89f7-4485-ae6b-4b82da30cf39","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    {"id":"11b95f60-49ba-4be6-b565-420a262b840f","personEmail":"jackson@gokdis.ecosys.eu","productId":"832a26b2-82c3-485e-8fa0-36de9242cc7f","description":"","quantity":1,"time":"2024-04-23 15:30:00"},
    
])

product_df = pd.DataFrame([{"id":"3a3d1d46-b1ef-4154-b88c-035d16e46ac2","sectionId":"63cd2dcd-e1b3-4b53-98c5-dc079db97fcc",
                 "name":"cereal","description":"Healthy and nutritious baby food","stock":60,"price":2.99},
                {"id":"67a2a0d1-5628-4d0a-94cb-505ab86b98d3","sectionId":"408ce76e-c6c1-4819-a47a-456627dd7d56",
                 "name":"preserved dips spreads","description":"Variety pack of delicious frozen desserts","stock":70,"price":8.99},
                {"id":"904f16e7-92b7-4a97-a0fd-4580843427af","sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac",
                 "name":"butter","description":"Durable and absorbent paper towels","stock":150,"price":2.99},
                {"id":"d9a9be6b-76df-43a0-9bfb-e3fc0dc3494e","sectionId":"b516b990-8cd1-4152-9c3f-9049cb14086d",
                 "name":"packaged poultry","description":"Soft and fresh sliced bread","stock":40,"price":2.49},
                {"id":"abba64c4-88a5-403a-ba27-6888a2c2b0eb","sectionId":"4816bbae-6670-4253-a47f-e7eac1f32b2b",
                 "name":"oral hygiene","description":"Strong and durable large garbage bags","stock":100,"price":10.99},
                {"id":"4b0a1f9e-3f4c-4df9-a86f-9a7c3507b170","sectionId":"1c292782-1120-4498-aedf-873b45b29046",
                 "name":"bakery desserts","description":"Perfect for entertaining guests","stock":50,"price":19.99},
                {"id":"895c0f44-295e-498d-9fd2-3eb12163655b","sectionId":"53cc11d0-4014-42c0-ac0f-42b7e84a9e7a","name":"latino foods","description":"Creamy and flavorful salted butter","stock":80,"price":3.99},{"id":"0be0f5f0-5d17-4d7d-bc19-8c201d31a5e5","sectionId":"2d69e9b6-f927-4732-8a97-93a27691ede8","name":"popcorn jerky","description":"Traditional soy sauce for seasoning","stock":60,"price":2.99},{"id":"234a385d-9cf6-47e1-89c6-48a325b9924c","sectionId":"408ce76e-c6c1-4819-a47a-456627dd7d56","name":"pickled goods olives","description":"Variety pack of delicious bakery snacks","stock":80,"price":5.99},{"id":"05e4bf6a-19f5-49d8-8d7d-26be01562850","sectionId":"b516b990-8cd1-4152-9c3f-9049cb14086d","name":"poultry counter","description":"French-style baguettes ready to bake","stock":40,"price":3.49},{"id":"2b1c3e36-5299-4744-a0a1-314c3a5d3d43","sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac","name":"milk","description":"Healthy and delicious whole grain bagels","stock":50,"price":4.99},{"id":"7ad93ec8-d7fb-4ed9-81d7-18b70a92921a","sectionId":"408ce76e-c6c1-4819-a47a-456627dd7d56","name":"condiments","description":"Rich and creamy vanilla yogurt","stock":60,"price":2.49},{"id":"f0f4604e-9d2b-422e-9fc0-20a97acaa013","sectionId":"1c292782-1120-4498-aedf-873b45b29046","name":"buns rolls","description":"Gentle diapers for sensitive skin","stock":200,"price":29.99},{"id":"83fbd7b6-6cfb-4c94-ba9a-8b3d79179e84","sectionId":"2e7e3c54-c5c9-4d99-9c6f-fb38117f3126","name":"canned meals beans","description":"Fresh whole chickens ready to cook","stock":30,"price":9.99},{"id":"eaa6c2a7-f5ae-4a5c-a4b1-cfcfe63b8327","sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e","name":"energy sports drinks","description":"Crunchy and tangy dill pickles","stock":50,"price":2.49},{"id":"1fd80f53-f837-4dc1-af4d-36b2e7b1384e","sectionId":"dc41e23f-9919-498e-a894-883640033a05","name":"missing","description":"Premium quality long-grain white rice","stock":80,"price":5.49},{"id":"5e49b490-3a2b-4579-aa6f-b07a83784e58","sectionId":"2d69e9b6-f927-4732-8a97-93a27691ede8","name":"chips pretzels","description":"Long-lasting fresh scent deodorant","stock":80,"price":4.49},{"id":"5d6cf6d7-4e43-4478-b3cb-99dbd4db49a3","sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e","name":"coffee","description":"Healthy whole wheat tortillas for wraps","stock":60,"price":2.99},{"id":"c29d83d4-8b5c-44b3-b1c1-f9eb0b7486f2","sectionId":"98e916e3-f6da-4e2c-8537-8fc63872512f","name":"frozen breads doughs","description":"Variety pack of assorted greeting cards","stock":90,"price":4.99},{"id":"cc9c8f51-45d8-4fa8-b7c7-dc10e3e3b4a2","sectionId":"9651a328-c842-4965-8f45-b592a5bd5ddb","name":"fresh vegetables","description":"Variety pack of quality meats","stock":50,"price":15.99},{"id":"1a51b251-d76c-4f37-ba94-d77c79d8e5db","sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e","name":"juice nectars","description":"Smooth and creamy cream cheese","stock":40,"price":3.99},{"id":"e0e56e9e-cb68-4269-98d5-3a06bb58bc8f","sectionId":"5134cede-8ca7-4e15-ab3d-64362b495d48","name":"lunch meat","description":"Effective pain relief tablets","stock":150,"price":9.99},{"id":"36d1e155-220d-41e6-91a4-00d16629e4bb","sectionId":"4816bbae-6670-4253-a47f-e7eac1f32b2b","name":"soap","description":"Comfortable and reliable tampons","stock":100,"price":6.99},{"id":"144206f3-7f14-4d6e-b2f2-5f43762b85f0","sectionId":"b516b990-8cd1-4152-9c3f-9049cb14086d","name":"meat counter","description":"Gentle and moisturizing hand soap","stock":90,"price":3.99},{"id":"2f5dc69f-4e52-47aa-99b4-7c35a4c2a717","sectionId":"5134cede-8ca7-4e15-ab3d-64362b495d48","name":"fresh dips tapenades","description":"Spicy and flavorful salsa made with authentic Mexican ingredients","stock":50,"price":2.99},{"id":"1d2b3f56-36cb-4fa3-b7e7-c6c6a5f5a460","sectionId":"63cd2dcd-e1b3-4b53-98c5-dc079db97fcc","name":"granola","description":"Classic spaghetti pasta for your favorite recipes","stock":70,"price":1.99},{"id":"5d14b2df-2f1a-447a-b6c3-d892f0a9dc8e","sectionId":"4816bbae-6670-4253-a47f-e7eac1f32b2b","name":"muscles joints pain relief","description":"Assorted fruit-flavored snacks for all ages","stock":100,"price":3.99},{"id":"ff9c93f2-8b2c-484e-bc27-7abcf0135d97","sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac","name":"other creams cheeses","description":"Healthy whole wheat hamburger buns","stock":30,"price":3.99},{"id":"69d36e53-1b92-42c1-a5ec-71e9f8e2f50b","sectionId":"b516b990-8cd1-4152-9c3f-9049cb14086d","name":"hot dogs bacon sausage","description":"Versatile cleaner for various surfaces","stock":70,"price":4.99},{"id":"c302f180-92af-466b-9eab-85f1d2795c2b","sectionId":"9651a328-c842-4965-8f45-b592a5bd5ddb","name":"packaged vegetables fruits","description":"Tasty and nutritious beef-flavored dog food","stock":120,"price":15.99},{"id":"cb009bc2-eb25-4a07-af32-34d72f816ad2","sectionId":"5134cede-8ca7-4e15-ab3d-64362b495d48","name":"prepared soups salads","description":"Versatile marinade sauce for meat and vegetables","stock":40,"price":3.49},{"id":"65a31b05-40da-457d-a0e4-d8e23fb20194","sectionId":"2d69e9b6-f927-4732-8a97-93a27691ede8","name":"nuts seeds dried fruit","description":"Gentle and moisturizing shampoo for all hair types","stock":60,"price":5.99},{"id":"cfa7fe5e-7d8b-4e4a-9c94-9c5f89573c30","sectionId":"c31db0cc-e796-44b8-8239-6c9a3cc51e95","name":"diapers wipes","description":"Powerful bleach for cleaning and disinfecting","stock":50,"price":3.49},{"id":"fd542d1d-9b45-48ac-9b6f-0e9d6e3d0ac4","sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac","name":"yogurt","description":"Rich and flavorful smoked bacon","stock":75,"price":6.99},{"id":"ce689c97-787a-4793-a587-6a68c5d53cf3","sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac","name":"packaged cheese","description":"Certified halal chicken breast","stock":80,"price":7.99},{"id":"7a8b8d71-ee3e-4a05-9241-24e001b73852","sectionId":"408ce76e-c6c1-4819-a47a-456627dd7d56","name":"baking ingredients","description":"","stock":100,"price":1.99},{"id":"7e22f17b-4c3b-472e-8e20-d46f5be0f3d0","sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e","name":"refrigerated","description":"Rich and creamy heavy cream for cooking","stock":50,"price":3.99},{"id":"1b1b3c67-3ae8-47d4-82c0-b0f75ab3a7b5","sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac","name":"eggs","description":"Refreshing mint toothpaste for clean teeth","stock":100,"price":4.49},{"id":"e93c02de-6ff3-4763-8a13-4cf5a4cb7bf7","sectionId":"2e7e3c54-c5c9-4d99-9c6f-fb38117f3126","name":"canned fruit applesauce","description":"Decadent and rich chocolate ice cream","stock":50,"price":6.99},{"id":"a65a1cfd-3d9c-4e34-84e3-f60785de6b26","sectionId":"d1fb5bbc-e358-4039-8ce0-f2f4ef8f328f","name":"food storage","description":"Effective liquid laundry detergent","stock":80,"price":7.99},{"id":"3ed8ef8d-d874-4c6f-8711-0eb96b4c54c5","sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac","name":"soy lactosefree","description":"Comfortable and absorbent toilet paper","stock":200,"price":3.49},{"id":"a4f64f5a-c0c8-45b2-94a2-5a3acbf09a7d","sectionId":"408ce76e-c6c1-4819-a47a-456627dd7d56","name":"honeys syrups nectars","description":"Nutritious multigrain packaged bread","stock":50,"price":4.49},{"id":"a875c70b-c5ed-43fc-8fc9-7d95b85d9e01","sectionId":"98e916e3-f6da-4e2c-8537-8fc63872512f","name":"ice cream ice","description":"Indulgent chocolate cake for dessert","stock":20,"price":12.99},{"id":"b2b68b4b-99b4-4199-aa5e-24eab8f5433f","sectionId":"d1fb5bbc-e358-4039-8ce0-f2f4ef8f328f","name":"plates bowls cups flatware","description":"Pure and refreshing orange juice","stock":60,"price":5.99},{"id":"832a26b2-82c3-485e-8fa0-36de9242cc7f","sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e","name":"tea","description":"Conveniently packaged pork chops","stock":25,"price":14.99},{"id":"a7e92d33-c046-4f5a-8d2f-002de73e1266","sectionId":"98e916e3-f6da-4e2c-8537-8fc63872512f","name":"frozen breakfast","description":"Variety pack of deli meats","stock":30,"price":17.99},{"id":"1fb7c6bb-5c90-4d26-bbcb-5af6efc6a692","sectionId":"e5650acf-0597-461c-85b8-5679c76df7ac","name":"cream","description":"Delicious salmon-flavored cat food","stock":50,"price":7.99},{"id":"6dd97df5-b86e-4c07-a4f4-f4df1c0143e9","sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e","name":"water seltzer sparkling water","description":"Easy-to-clean clumping cat litter","stock":100,"price":12.99},{"id":"f8a4586e-6768-45df-850b-5e312e67c2e9","sectionId":"f3853589-d1be-4eb1-b4b1-18cdaa78c63e","name":"soft drinks","description":"Farm-fresh large grade A eggs","stock":120,"price":4.99},{"id":"f1e5d0d0-89f7-4485-ae6b-4b82da30cf39","sectionId":"1c292782-1120-4498-aedf-873b45b29046","name":"bread","description":"Quick and easy meal option","stock":40,"price":10.99},{"id":"5a274914-b63c-4b82-8e54-aa14f49933bb","sectionId":"2d69e9b6-f927-4732-8a97-93a27691ede8","name":"energy granola bars","description":"Fresh and nutritious whole milk","stock":100,"price":2.49},{"id":"1b3fe663-036e-4e80-8536-d5880ddcc7fc","sectionId":"9651a328-c842-4965-8f45-b592a5bd5ddb","name":"fresh fruits","description":"Assorted snacks at a discounted price","stock":100,"price":8.99},{"id":"bc5ef720-2ee6-4e32-a2b3-2275f3f53907","sectionId":"d1fb5bbc-e358-4039-8ce0-f2f4ef8f328f","name":"paper goods","description":"Energy-efficient LED light bulbs","stock":200,"price":8.99}])



merged_df = pd.merge(position_df, cell_df, on=['x', 'y'])

# Step 2: Find the section ID from cell data
merged_with_section_names = pd.merge(merged_df, section_df, left_on='sectionId', right_on='id')

# Step 3: Find the section name from section data using section ID
merged_df = pd.merge(merged_df, section_df, left_on='sectionId', right_on='id')


def recommend_products(person):
    person_data = merged_df[merged_df['personEmail'] == person]
    print(person_data)
    # Count occurrences of each section ID
    section_id_counts = person_data['sectionId'].value_counts()
    
    # Filter section IDs occurring less than 2 times
    valid_section_ids = section_id_counts[section_id_counts >= 2].index
    
    # Filter products based on valid section IDs
    aisle_products = product_df[product_df['sectionId'].isin(valid_section_ids)]

    # Recommend unique products from those aisles
    recommendations = aisle_products['name'].unique()
    
    recommendations_list = recommendations.tolist()
    
    return recommendations_list


app = Flask(__name__)

@app.route('/')
def hello():
    
    return ""

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    person = request.args.get('person')
    
    recommendations = recommend_products(person)
    
    response = {'recommendations': recommendations}
    
    return jsonify(response)  

if __name__ == '__main__':
    app.run(debug=True)
