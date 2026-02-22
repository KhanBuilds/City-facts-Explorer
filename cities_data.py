# City facts database - 10 facts for each city

CITIES_FACTS = {
    # World Cities
    "Tokyo": [
        "Tokyo is the most populous metropolitan area in the world with over 37 million people.",
        "The city has more Michelin-starred restaurants than any other city in the world.",
        "Tokyo was originally called Edo and was renamed Tokyo in 1868, meaning 'Eastern Capital'.",
        "The city hosted the Summer Olympics in 1964 and 2021 (delayed from 2020).",
        "Tokyo's Shibuya Crossing is one of the busiest pedestrian crossings in the world.",
        "The Tokyo Stock Exchange is the third-largest stock exchange in the world by market value.",
        "Tokyo has the world's largest fish market, Tsukiji Outer Market (formerly Tsukiji Market).",
        "The city sits on the Pacific Ring of Fire and experiences frequent earthquakes.",
        "Tokyo Tower, inspired by the Eiffel Tower, is 13 meters taller than its French counterpart.",
        "The Greater Tokyo Area produces about one-third of Japan's total GDP."
    ],
    
    "New York": [
        "New York City is known as 'The Big Apple' and 'The City That Never Sleeps'.",
        "Central Park spans 843 acres and is visited by over 42 million people annually.",
        "The Statue of Liberty was a gift from France and was dedicated in 1886.",
        "NYC has the largest subway system in North America with 472 stations.",
        "Manhattan was purchased from Native Americans for goods worth about $24 in 1626.",
        "Times Square is visited by over 50 million tourists annually.",
        "The city has over 800 languages spoken, making it the most linguistically diverse city in the world.",
        "Wall Street is home to the New York Stock Exchange, the world's largest stock exchange.",
        "The Empire State Building was the world's tallest building from 1931 to 1971.",
        "NYC produces about 14,000 tons of trash daily."
    ],
    
    "London": [
        "London is the capital of England and has been a major settlement for over 2,000 years.",
        "The London Underground, known as 'The Tube', is the oldest underground railway network in the world.",
        "Big Ben is actually the name of the bell, not the clock tower itself (officially Elizabeth Tower).",
        "London has more green space than any other major city of comparable size.",
        "The city is home to four UNESCO World Heritage Sites.",
        "London Bridge and Tower Bridge are two different bridges - a common source of confusion.",
        "The Great Fire of London in 1666 destroyed most of medieval London.",
        "London has been the host city of the Summer Olympics three times: 1908, 1948, and 2012.",
        "The city has over 170 museums, including the British Museum and Tate Modern.",
        "London's financial district, known as 'The City', is just one square mile in area."
    ],
    
    "Paris": [
        "Paris is known as 'The City of Light' due to its early adoption of street lighting.",
        "The Eiffel Tower was built for the 1889 World's Fair and was initially meant to be temporary.",
        "The Louvre Museum is the world's largest art museum and houses the Mona Lisa.",
        "Paris has 20 arrondissements (districts) arranged in a spiral pattern from the center.",
        "The city is built on both banks of the Seine River and includes two natural islands.",
        "Notre-Dame Cathedral took nearly 200 years to complete (1163-1345).",
        "Paris Metro has 302 stations and no point in Paris is more than 500 meters from a station.",
        "The Arc de Triomphe honors those who fought and died for France in various wars.",
        "Paris Fashion Week is one of the 'Big Four' fashion weeks along with Milan, London, and New York.",
        "The city has over 400 parks and gardens, including the famous Tuileries and Luxembourg Gardens."
    ],
    
    "Rome": [
        "Rome is known as 'The Eternal City' and 'Caput Mundi' (Capital of the World).",
        "The Colosseum could hold between 50,000 and 80,000 spectators at its peak.",
        "Vatican City, located within Rome, is the smallest sovereign nation in the world.",
        "Rome was built on seven hills: Aventine, Caelian, Capitoline, Esquiline, Palatine, Quirinal, and Viminal.",
        "The Pantheon has the world's largest unreinforced concrete dome, built in 126 AD.",
        "Ancient Romans built over 250,000 miles of roads throughout their empire.",
        "The Trevi Fountain collects about €3,000 in coins daily, which is donated to charity.",
        "Rome has more fountains than any other city in the world - over 2,000.",
        "The city has been continuously inhabited for over 2,800 years.",
        "St. Peter's Basilica took 120 years to complete and involved architects like Michelangelo and Bernini."
    ],
    
    "Sydney": [
        "Sydney Opera House is a UNESCO World Heritage Site and architectural masterpiece.",
        "The Sydney Harbour Bridge is nicknamed 'The Coathanger' due to its arch-based design.",
        "Sydney is the largest city in Australia but not the capital (that's Canberra).",
        "The city has over 100 beaches, including the famous Bondi and Manly beaches.",
        "Sydney Harbour is one of the world's largest natural harbors.",
        "The Royal Botanic Gardens Sydney are home to over 30,000 plant specimens.",
        "Sydney was the first city in the world to see in the year 2000's millennium celebrations.",
        "The city hosted the Summer Olympics in 2000, considered one of the most successful Games ever.",
        "Sydney's CBD is built around one of the world's finest natural harbors.",
        "The Blue Mountains, a UNESCO World Heritage area, are just 90 minutes from Sydney."
    ],
    
    "Dubai": [
        "Dubai is home to the Burj Khalifa, the world's tallest building at 828 meters.",
        "The city has the world's largest shopping mall by total area - Dubai Mall.",
        "Dubai's economy was built on oil but now relies heavily on tourism, aviation, and real estate.",
        "The Palm Jumeirah is an artificial island shaped like a palm tree, visible from space.",
        "Dubai International Airport is one of the world's busiest airports by passenger traffic.",
        "The city has no permanent rivers but has created over 50km of man-made beaches.",
        "Dubai Gold Souk is one of the largest gold markets in the world.",
        "The Burj Al Arab hotel costs over $1,000 per night and is often called the world's only 7-star hotel.",
        "Dubai has plans to have 25% of all transportation be autonomous by 2030.",
        "The city experiences less than 5mm of rainfall per year on average."
    ],
    
    "Singapore": [
        "Singapore is both a city and a country, officially the Republic of Singapore.",
        "The city-state has four official languages: English, Malay, Mandarin, and Tamil.",
        "Singapore Changi Airport has been voted the world's best airport multiple times.",
        "The Marina Bay Sands hotel has an infinity pool 57 stories above ground.",
        "Singapore has one of the world's highest rates of millionaires per capita.",
        "The city has strict laws, including fines for chewing gum and jaywalking.",
        "Singapore's Botanic Gardens is the country's first UNESCO World Heritage Site.",
        "The city-state imports about 90% of its food from other countries.",
        "Singapore has transformed from a developing to developed nation in just one generation.",
        "The Merlion, half-fish half-lion, is Singapore's national symbol and mascot."
    ],
    
    "Moscow": [
        "Moscow is the largest city in Europe with over 12 million inhabitants.",
        "The Kremlin is a fortified complex at the heart of Moscow and houses the Russian government.",
        "Red Square is not named for communism but for the Russian word 'krasnaya' meaning beautiful.",
        "Moscow Metro is famous for its ornate stations, often called 'underground palaces'.",
        "The city has more billionaires than any other city in the world.",
        "Moscow State University's main building was the tallest building in Europe until 1997.",
        "The Bolshoi Theatre is one of the most renowned ballet and opera theaters in the world.",
        "Moscow experiences a continental climate with very cold winters and warm summers.",
        "Saint Basil's Cathedral with its colorful onion domes is Moscow's most recognizable landmark.",
        "The city spans 11 time zones, though it operates on Moscow Standard Time."
    ],
    
    "Cairo": [
        "Cairo is known as 'The City of a Thousand Minarets' due to its Islamic architecture.",
        "The Great Pyramid of Giza, near Cairo, is the only surviving Wonder of the Ancient World.",
        "Cairo has the largest urban area in Africa and the Arab world.",
        "Al-Azhar University, founded in 970 AD, is one of the oldest continuously operating universities.",
        "The city sits on both banks of the Nile River near the Nile Delta.",
        "Khan el-Khalili bazaar has been a major trading hub for over 600 years.",
        "Cairo's Egyptian Museum houses the world's largest collection of ancient Egyptian artifacts.",
        "The Citadel of Saladin offers panoramic views of the entire city.",
        "Cairo is nicknamed 'Umm al-Dunya', meaning 'Mother of the World' in Arabic.",
        "The city experiences very little rainfall, receiving less than an inch per year on average."
    ],

    # Pakistani Cities
    "Karachi": [
        "Karachi is Pakistan's largest city and commercial capital with over 15 million people.",
        "The city was the first capital of Pakistan from 1947 to 1958.",
        "Karachi Port is one of the largest and busiest seaports in the region.",
        "The city is known as the 'City of Lights' due to its vibrant nightlife and illumination.",
        "Karachi contributes about 20% of Pakistan's total GDP.",
        "Mazar-e-Quaid houses the tomb of Pakistan's founder, Quaid-e-Azam Muhammad Ali Jinnah.",
        "The city has the largest urban forest in the world - Safari Park covers 2,400 acres.",
        "Karachi was once called the 'Pearl of the Arabian Sea'.",
        "The National Stadium Karachi can hold 34,000 spectators and hosts international cricket matches.",
        "Clifton Beach is one of the most popular beaches in Pakistan, stretching for miles along the Arabian Sea."
    ],
    
    "Lahore": [
        "Lahore is known as the 'Heart of Pakistan' and cultural capital of the country.",
        "The city is famous for its Mughal architecture, including the Badshahi Mosque and Lahore Fort.",
        "Lahore's Walled City is a UNESCO World Heritage Site with 13 historic gates.",
        "The city is renowned for its food culture, particularly street food in areas like Food Street.",
        "Shalimar Gardens, built by Emperor Shah Jahan, is a masterpiece of Mughal garden design.",
        "Lahore Museum houses one of the largest collections of Buddhist art in the world.",
        "The city hosts the annual Basant festival, famous for colorful kite flying.",
        "Lahore College for Women was the first degree college for women in Punjab, established in 1922.",
        "The Lahore Resolution was passed here in 1940, calling for the creation of Pakistan.",
        "Data Darbar is one of the largest Sufi shrines in South Asia, attracting millions of pilgrims."
    ],
    
    "Islamabad": [
        "Islamabad is the capital of Pakistan, purpose-built in the 1960s to replace Karachi.",
        "The city is known for its modern architecture and urban planning, designed by Greek architect Constantinos Doxiadis.",
        "Faisal Mosque is one of the largest mosques in the world and an iconic symbol of Islamabad.",
        "The city is located in the Pothohar Plateau near the Margalla Hills.",
        "Islamabad is consistently ranked among the most beautiful capitals in the world.",
        "The Pakistan Monument represents the four provinces and three territories of Pakistan.",
        "Daman-e-Koh offers panoramic views of the entire city from the Margalla Hills.",
        "The city is planned in a series of zones including diplomatic, residential, and commercial areas.",
        "Lok Virsa Museum showcases Pakistan's rich cultural heritage and folk traditions.",
        "Islamabad has one of the lowest crime rates among major cities in Pakistan."
    ],
    
    "Rawalpindi": [
        "Rawalpindi is known as the 'Twin City' of Islamabad, located just 14 km away.",
        "The city serves as the headquarters of the Pakistan Army.",
        "Rawalpindi was an important military cantonment during British colonial rule.",
        "Raja Bazaar is one of the oldest and busiest markets in the city.",
        "The city is a major transportation hub connecting northern Pakistan with the rest of the country.",
        "Ayub National Park is a popular recreational area with a lake and boating facilities.",
        "Rawalpindi Cricket Stadium has hosted numerous international cricket matches.",
        "The city experiences four distinct seasons with hot summers and mild winters.",
        "Rawalpindi Museum showcases the cultural history of the Pothohar region.",
        "The Grand Trunk Road, one of Asia's oldest and longest major roads, passes through Rawalpindi."
    ],
    
    "Faisalabad": [
        "Faisalabad is known as the 'Manchester of Pakistan' due to its textile industry.",
        "The city is the third-largest city in Pakistan and the second-largest in Punjab.",
        "Faisalabad contributes significantly to Pakistan's textile exports.",
        "The city was originally called Lyallpur after the British administrator James Lyall.",
        "Clock Tower (Ghanta Ghar) is the central landmark and symbol of Faisalabad.",
        "University of Agriculture, Faisalabad is one of the leading agricultural universities in Asia.",
        "The city is built in a unique pattern with eight roads radiating from the central Clock Tower.",
        "Faisalabad is a major hub for cotton production and processing in Pakistan.",
        "Chenab Club is one of the oldest recreational clubs in the city, established during British rule.",
        "The city plays a crucial role in Pakistan's economy, particularly in agriculture and textiles."
    ],
    
    "Multan": [
        "Multan is known as the 'City of Saints' due to numerous Sufi shrines located here.",
        "The city is one of the oldest continuously inhabited cities in Asia, dating back 5,000 years.",
        "Multan is famous for its handicrafts, particularly blue pottery and camel-skin products.",
        "The shrine of Bahauddin Zakariya is a major pilgrimage site for Sufi Muslims.",
        "Multan Fort is an ancient structure that has been rebuilt several times throughout history.",
        "The city is a major center for mango production, known for its sweet and juicy varieties.",
        "Multan Cricket Stadium has hosted international cricket matches and is a modern facility.",
        "The city experiences extremely hot summers with temperatures often exceeding 45°C (113°F).",
        "Shah Rukn-e-Alam's tomb is considered one of the finest examples of early Islamic architecture.",
        "Multan is strategically located at the crossroads of four provinces of Pakistan."
    ],
    
    "Peshawar": [
        "Peshawar is the capital of Khyber Pakhtunkhwa and gateway to the historic Khyber Pass.",
        "The city is one of the oldest continuously inhabited cities in South Asia, over 2,000 years old.",
        "Peshawar Museum houses one of the world's finest collections of Gandhara art and Buddhist sculptures.",
        "The old walled city of Peshawar retains much of its traditional Mughal and Afghan architecture.",
        "Qissa Khwani Bazaar, meaning 'Market of Storytellers', is a famous traditional market.",
        "The University of Peshawar is one of the oldest universities in Pakistan, established in 1950.",
        "Peshawar is known for its rich Pashtun culture, hospitality, and traditional cuisine.",
        "The city has been an important center of trade between Central Asia and South Asia for centuries.",
        "Mahabat Khan Mosque is a beautiful 17th-century Mughal mosque in the heart of the city.",
        "Peshawar experiences a semi-arid climate with hot summers and mild winters."
    ],
    
    "Quetta": [
        "Quetta is the capital of Balochistan, Pakistan's largest province by area.",
        "The city is known as the 'Fruit Garden of Pakistan' due to its orchards and fruit production.",
        "Quetta is located in the Quetta Valley, surrounded by mountains on all sides.",
        "The city experiences a continental climate with cold winters due to its high elevation (1,680 meters).",
        "Ziarat, near Quetta, is famous for its juniper forests and was Muhammad Ali Jinnah's last residence.",
        "The Staff College Quetta is a prestigious military institution that trains officers from around the world.",
        "Quetta's location makes it strategically important, near the borders of Afghanistan and Iran.",
        "The city is known for its traditional Balochi handicrafts, including carpets and embroidery.",
        "Hanna Lake is a popular recreational spot and picnic destination near Quetta.",
        "The University of Balochistan, established in 1970, is the province's premier educational institution."
    ],
    
    "Sialkot": [
        "Sialkot is world-renowned for manufacturing sports goods, especially footballs and cricket equipment.",
        "The city produces about 70% of the world's hand-stitched footballs, including for FIFA World Cups.",
        "Sialkot is the birthplace of Allama Iqbal, Pakistan's national poet and philosopher.",
        "The city has a strong export-oriented economy, particularly in sports goods and surgical instruments.",
        "Sialkot International Airport is Pakistan's first privately owned public airport.",
        "The city is famous for its surgical instruments, which are exported worldwide.",
        "Iqbal Manzil is the ancestral home of Allama Iqbal and now serves as a museum.",
        "Sialkot's craftsmen are skilled in leather work, producing high-quality leather products for export.",
        "The city hosts the annual Sialkot Chamber of Commerce sports goods exhibition.",
        "Sialkot is located near the India-Pakistan border in the fertile Punjab region."
    ],
    
    "Gujranwala": [
        "Gujranwala is known as the 'City of Wrestlers' due to its strong wrestling tradition.",
        "The city is famous throughout Pakistan for its delicious traditional foods, especially Gujranwala-style chicken.",
        "Gujranwala is an important industrial center, particularly for textiles and agriculture.",
        "The city is the birthplace of Maharaja Ranjit Singh, the famous Sikh ruler of Punjab.",
        "Ranjit Singh's haveli (mansion) is now a museum dedicated to his life and reign.",
        "The city is known for its skilled metalworkers and traditional crafts.",
        "Gujranwala has a rich cultural heritage with influences from Sikh, Muslim, and Hindu traditions.",
        "The city experiences a typical Punjab climate with hot summers and cool winters.",
        "Jinnah Stadium Gujranwala is a major venue for cricket and other sports in the region.",
        "The city is well-connected by road and rail to major cities like Lahore, Islamabad, and Karachi."
    ],
    
    "Sargodha": [
        "Sargodha is known as the 'City of Eagles' due to the Pakistan Air Force College located here.",
        "The city is famous for producing the finest citrus fruits in Pakistan, especially Kinnow oranges.",
        "Sargodha is home to the University of Sargodha, established in 2002 as a major educational institution.",
        "The Pakistan Air Force College Sargodha is one of the most prestigious military training institutions in the country.",
        "The city serves as the headquarters of Sargodha Division and is an important administrative center.",
        "Sargodha's agricultural economy is built around citrus cultivation, wheat, rice, and sugarcane production.",
        "The Kinnow orange variety developed in Sargodha is exported worldwide and is a major source of foreign exchange.",
        "Sargodha Cricket Stadium has hosted several domestic and international cricket matches.",
        "The city is strategically located on the Grand Trunk Road, connecting it to major Pakistani cities.",
        "Sargodha's Satellite Town is a well-planned residential area known for its modern infrastructure and amenities."
    ]
}