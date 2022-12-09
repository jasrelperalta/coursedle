import random
from termcolor import colored

dict_A = {"ABME" : ["Agribusiness Management and Entrepreneurship", "Agribusiness management encompasses many aspects of the economy: agricultural producers, businesses that provide supplies and services to the producers, businesses that add value to agricultural products, and those that facilitate the marketing of agricultural products to an ever-growing marketplace"],
          "ABSE" : ["Agrometeorology, Bio-structures and Environment Engineering", "Aims to: harness crop yield potential from favourable weather as well as weather extremes; improve crop and animal production by developing controlled environment technologies; and minimize environmental impact of agricultural wastes"],
          "AGCM" : ["Agricultural Chemistry", "The program prepares its students to become full-fledged chemists who are specially trained to tackle chemistry problems related to food and agriculture in support of the agricultural and rural development thrusts of the country."],
          "AGME" : ["Agrometeorology", "Agrometeorology deals with a wide-spectrum of subjects comprising all the weather-sensitive components of the chain from agricultural production to consumption."],
          "AECO" : ["Agricultural Economics", "The BS Agricultural and Applied Economics program aims to produce students who: (1) have technical background in agriculture and related sciences, (2) have understanding of the economic theories and tools in analyzing issues and problems in the agriculture and related sectors, and (3) are able to provide insights on policies and strategies relating to sustainable agricultural and rural development."],
          "AENG" : ["Agricultural Engineering", "It is designed to produce graduates who possess knowledge and skills in the application of engineering principles for the production, processing, handling and storage of food, fiber and materials of biological origin."],
          "AERS" : ["Agricultural Education and Rural Studies", "Aims to prepare graduate students to take leading roles in dealing with problems and opportunities in rural communities as they relate to the society as a whole. The program focuses on sustainable rural communities characterized by long term well-being based on the integration of social, cultural, economic, and environmental factors in their planning."],
          "AFBE" : ["Agricultural, Food and Bioprocess Engineering", "Under Institute of Agricultural and Biosystems Engineering (IABE), College of Engineering and Agro-Industrial Technology."],
          "AGRI" : ["Agriculture", "Aims to educate students towards a career in scientifically-based sustainable agriculture, to enable them to develop and effectively manage a self-reliant and economically viable agriculture-related enterprise and to prepare them to become professionals with social commitment."],
          "AGRS" : ["Agrarian Studies", "Under Institute of Governance and Rural Development, College of Public Affairs and Development"],
          "AMAT" : ["Applied Mathematics", "Students of the program will be trained to apply these principles and methods to solve decision making problems by developing mathematical models and algorithms."],
          "AMPE" : ["Agribiosystem, Machinery, Power Engineering", "Under  Agribiosystems Machinery and Power Engineering Division (AMPED), Institute of Agricultural and Biosystems Engineering"],
          "ANSC" : ["Animal Science", "Covers a variety of specializations which includes Animal Breeding, Animal Physiology, Animal Nutrition, Animal Production, Dairy Technology and Meat Science"],
          "ANTH" : ["Anthropology", "It is a social science that explores society and humanity from a bio-cultural and cross-cultural approach."],
          "APHY" : ["Applied Physics", "Is a category of physics where fundamental discoveries in physics drive the creation, invention, and innovation of practical devices and systems. It has produced technological breakthroughs with profound effects to the development of modern civilization."],
          "ARDS" : ["Agrarian and Rurban Development Studies", "It is intended to train both practitioners serving government and non-government institutions as well as scholars dedicated to the analysis of public issues, particularly as they relate to the improvement of public welfare."],
          "ARTS" : ["Arts", "Under Department of Humanities (DHUM), College of Arts and Sciences"],
          "ASYS" : ["Agricultural System", "Under the Agricultural Systems Institute (ASI), first cluster in the College of Agriculture to be established in 2003"],
          }

dict_C = {"CERP" : ["Community and Environmental Resource Planning", "Under the College of Human Ecology. It functions within the harmonizing framework of humans in relation to their environment. Its ultimate aim is to contribute towards the national goal of improving the quality of life and general well-being of the Filipino people."],
          "CHEM" : ["Chemistry", "These courses are designed to produce highly trained chemistry practitioners for industry as well as academic and research institutions who can engage in industry practice, teaching, research, development and extension work in all areas of basic and applied chemistry."],
          "CMSC" : ["Computer Science", "These courses emphasizes strength of technical preparation and produces graduates highly capable of working in the computer industry and pursuing graduate studies in Computer Science. A solid technical background complemented by experience on real systems provide the students tools to handle the most demanding aspects of systems development, data management and scientific computing."],
          "COMA" : ["Communication Arts", "These courses aims to help produce graduates who demonstrate proficiency in various theories of language, communication, literature, and performance, and exhibit analytical and integrative skills in the application of these theories in the cultural and creative industries and other settings."],
          "COMM" : ["Communication", "Under the College of Development Communication (CDC). It focuses on the theories and frameworks of communication in various contexts"],
          "COST" : ["Cooperative Studies", "The COST courses range from the broad concept of collective action to the basic theories and principles of cooperatives and the practical applications of cooperative models and practices. These courses aim to raise awareness and knowledge on the 'Cooperative Identity' and to promote the cooperative way of doing business and problem solving for socioeconomic and welfare development."],
          "CRPT" : ["Crop Protection", "Under the College of Agriculture and Food Science. It encompases topics inlcuding the principles of crop protection and integrated pest management"],
          "CRSC" : ["Crop Science", "These courses shall promote science-based, modern and sustainable agriculture and develop competent and responsible crop scientists and professionals, and generate sound scientific ideas, concepts, technologies, products and processes within the domains of crop science that are relevant to the needs and requirements of Philippine agriculture and end-user communities."]}

dict_D = {"DEVC": ["Development Communication", "The College of Development Communication (CDC) is the pioneer in the practice and study of development communication in Asia."],
          "DVST": ["Development Studies", "Tackles development issues such as food security, natural resource management, population, gender and development, and agrarian and rural development—areas that will support the distinctive excellence of UPLB in agriculture, forestry and the environment."]}

dict_E = {"ECON": ["Economics", "This program plays a prominent role in economics education, research, and public service in the Philippines; and  contribute to the formulation of local and national economic development plans through problem-oriented research and rigorous academic training that produce influential decision-makers in government, business, and civil society "],
          "EDUC": ["Educational Foundations", "Examines concepts and theories from educational, social, and developmental psychology and sociology"],
          "ENSC": ["Engineering Science", "The application of scientific and practical knowledge to design, analyze, and build structures, machines, and programs for practical purposes."],
          "ENTR": ["Entrepreneurship", "Viewed as change, generally entailing risk beyond what is normally encountered in starting a business, which may include other values than simply economic ones."]}

dict_F = {"FPPS": ["Forest Products and Paper Science", "The program aims to produce licensed foresters who are equipped with the foresters who are equipped with the knowledge and skills in making profitable but sustainable use of the basic properties of forest products, of technologies for maximizing their use and of their possible impacts to the environment."],
          "FRCH": ["French", "One of the foreign language programs offered by the Language Division of the Department of Humanities. It includes the fundamental elements of the French language within a cultural context with emphasis on pronunciation, vocabulary building, and conversation."]}


dict_H_L = {"HFDS": ["Human and Family Development Studies", "Study, promotion and application of human ecological approaches towards enhancing human development and family well-being across the lifespan."],
          "HIST": ["History", "Studies and investigates ancient and modern events and social trends."],
          "HORT": ["Horticolture", "A major field of study where a student may specialize in any of the following disciplines: Plant Breeding, Crop Production and Management, Crop Physiology Postharvest Science Landscaping"],
          "HUME": ["Human Ecology", "Uses interdisciplinary, holistic, and integrative approaches to understand human-environment interactions"],
          "LWRE": ["Land and Water Resources Engineering", "These coursesaims to provide formal training in land and water resources engineering, undertake research geared towards exploring solutions to relevant problems in land and water resources engineering, and Extend technical expertise and information about land and water resources engineering through consultancy, non-degree training programs and publications."]}

dict_M = {"MAED": ["Mathematics Education", "prepares students to understand the latest developments in the research and teaching of mathematics in order to impact future generations in an ever-changing society."],
          "MATH": ["Mathematics", "It has three tracks: Pure Mathematics, Applied Mathematics and Mathematics Education."]}

dict_N_R = {"NASC": ["Natural Science", "Natural Sciences are a group of disciplines that study the physical world and all the phenomena in nature. It is no longer offered in recent semesters in UPLB"],
          "NSTP": ["National Service Training Program", "NSTP is a program designed to develop the youth’s physical, moral, spiritual, intellectual, and social well-being and promote defense preparedness and ethics of service while undergoing training in any of its three program components. "]}

dict_P = {"PHDR": ["PHD by Research", "Includes Residency for PHD by Research"],
          "PHLO": ["Philosophy", "Emphasizes the role of research and extension in uncovering the richness of the Filipino mind embedded in Philippine culture, arts, politics, and folkways throughout Philippine history."],
          "PHYS": ["Physics", "Under the Institute of Mathematical Sciences and Physics (IMSP). It teaches students to understand and appreciate the natural world and aims to develop the quantitative analytical skills of the students."],
          "POSC": ["Political Science", "It includes the study of different systems of government, election processes, political parties, political ideology, historical analysis, political theory, changes in power and much more."],
          "PPTH": ["Plant Pathology", "It is the scientific study of plant diseases- their causes, interaction with host, taxonomy, biology, ecology, epidemiology, and development of management strategies."],
          "ROTC": ["Reserve Officers' Training Corps", "This is a program institutionalized under Sections 38 and 39 of Republic Act No. 7077 designed to provide military training to tertiary level students in order to motivate, train, organize and mobilize them for national defense preparedness"]}

dict_S = {"SFFG": ["Social Forestry and Forest government", "Natural Sciences are a group of disciplines that study the physical world and all the phenomena in nature. It is no longer offered in recent semesters in UPLB"],
          "SOSC": ["Social Science", "Social Science is a major category of academic disciplines that study human society and social relationships."],
          "SOIL": ["Soil Science", "Soil Science as a major field focuses on the understanding of the nature and properties of soils and how they relate to improvement on the uses of land particularly in agriculture."],
          "SPAN": ["Spanish", "Introduction to spoken and written Spanish, providing practice in listening, speaking, reading, writing and grammar. "],
          "SPCM": ["Speech Communication", "Those in speech communication are expected to apply principles and practices in speaking not only in the classroom set-up but also to various publics."],
          "SPEC": ["Speculative Thought", "Modern man’s heritage in speculative thought and philosophic method."],
          "SPPS": ["Strategic Planning and Policy Studies", "The program is designed to improve technical and practical knowledge and analytical skills in development planning and policy formulation and analysis; to enhance leadership qualities to advocate relevant policies for effective implementation of planned activities, monitoring progess and evaluation of development programs’ impacts; and to strengthen professional leverage and confidence in dealing with the resolution of policy issues and concerns."],
          "STAT": ["Statistics", "The program is designed to make a BS Statistics graduate flexible through exposure to the basic sciences, to build a career in business, industry, academe or government, or to pursue graduate studies in statistics and its allied fields."],
          "SUTC": ["Sugar Technology", "With solid background in both chemical engineering and sugar technology, it is hoped that this program will develop in the graduates the competency and proper perspective to meet the changing needs of the sugar industry and related agro-based industries."]}

dict_T = {"THEA": ["Theater Arts", "Theater Arts exposes students to the range of theater activities both onstage and offstage, all of which require an individual and collaborative intelligence and a passionate interest in theater."],
         "TMEM": ["Tropical Marine Ecosystems Management", "is an accelerated degree uniquely designed for professionals engaged in the management and governance of tropical marine ecosystems. It is under Shool of Environmental Science and Management (SESAM)"]}

dict_V = {"VEPI": ["Veterinary Epidemiology", "One of the many fields that falls within veterinary public health, veterinary epidemiology focuses specifically on disease surveillance, response, and prevention. It involves data collection and analysis to develop and test hypotheses related to disease patterns."],
          "VETA": ["Veterinary Anatomy", "Anatomy seeks to understand the structure, location and composition of the parts within organisms and their relationships with each other."],
          "VETC": ["Veterinary Clinics", "Demonstration of methods in clinical examination, diagnosis and treatment. Selected cases will be presented and discussed by the clinical staff together with senior students."],
          "VMCB": ["Veterinary Microbiology", "Classification  and general characteristics of bacteria, viruses, fungi and rickettsiae and fundamental microbiological techniques."],
          "VMED": ["Veterinary Medicine", "The students acquire both theoretical knowledge and practical experience in animal production and in the diagnosis, prevention, treatment, and control of diseases in companion, exotic, and farm animals, and are prepared to conduct research and extension activities. in companion, exotic and farm animals. "],
          "VPAR": ["Veterinary Parasitology", "Important arthropod and protozoan parasites of domestic animals; their morphology, biology, pathogenicity, transmission and control."],
          "VPHY": ["Veterinary Physiology", "A course under College of Veterinary Medicine (CVM) that focuses on the scientific study of the functional dynamics of animal biological systems and their relationship to the diagnosis and treatment of disease and injury."],
          "VPHM": ["Veterinary Pharmacology", "Introduces undergraduates to various drugs and other substances used in veterinary medicine."],
          "VPTH": ["Veterinary Pathology", "Principles of pathology and fundamentals of veterinary necropsy and histopathology up to Collection and examination of body fluids, secretions and excretions, with emphasis on interpretation of laboratory findings."],
          "VSUR": ["Veterinary Surgery", "Study includes General principles in veterinary anesthetic applications and surgical operation up to Principles and applications of radiography, ultrasonography, and other diagnostic imaging procedures in animals."]}

dict_W = {"WIKA": ["Wika, Kultura at Lipunan", "Pagsusuri sa ugnayan ng wika, kultura at lipunan"],
          "WLDL": ["Wildlife", " it is a graduate program thta provides students with the knowledge and skills in wildlife biology and techniques in research for conservation and management, with emphasis on Philippine wildlife."],
          "WSTH": ["Western Thought", "Western philosophy encompasses the philosophical thought and work of the Western world."]}

dict_A_Z = [dict_A, dict_C, dict_D, dict_E, dict_F, dict_H_L, dict_M, dict_N_R, dict_P, dict_S, dict_T, dict_V, dict_W] #comprehensive dictionary

#List of code per day
Monday = [dict_A]
Tuesday = [dict_C, dict_M]
Wednesday = [dict_D, dict_N_R]
Thursday = [dict_E, dict_P]
Friday = [dict_F, dict_S]
Saturday = [dict_T, dict_V]
Sunday = [dict_H_L, dict_W]

#SAMPLE CODE SELECTION 
item = random.choice(list(dict_A_Z))                #items in super dictionary dict_A_Z
pick = item                                         #store the selected item using pick
code_random = random.choice(list(pick.keys()))      #randomize through the selected sub dictionary
# print(code_random)

#sample/test printing the descriptions
'''
for code, desc in dict_A.items():
    print(colored(code, "blue"), end=": ")
    print(desc[0])
    print(desc[1])
    print()
'''



