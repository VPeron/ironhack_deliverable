### Introduction: Unveiling the Shadowed Threats to Nuclear Energy Infrastructure

In the age of digital interconnectedness, the world's critical infrastructure, including nuclear energy facilities, stands on the precipice of unprecedented vulnerability. The emergence of cyberspace as an arena for strategic conflict has given rise to a covert battlefield where unseen adversaries seek to exploit the vulnerabilities inherent in the technological fabrics of our modern world. Among the most concerning targets in this new age of warfare are nuclear energy plants, where the convergence of cutting-edge technology and global security interests has created an environment ripe for cyber intrusion.
The history of cyberattacks against nuclear energy plants is a tale of intrigue, technical prowess, and geopolitical tensions. It is a narrative that unfolds against the backdrop of humanity's quest for clean and efficient energy, juxtaposed with the relentless drive of cybercriminals and nation-state actors to infiltrate, disrupt, or even exploit these facilities. Within this complex narrative, we find a chronicle of events that range from early, rudimentary incidents to highly sophisticated, state-sponsored attacks, all posing grave threats to the safety, security, and stability of nuclear energy infrastructure.
This narrative begins with the early incidents in the 2000s, marked by the infamous ILOVEYOU virus and the ominous specter of Stuxnet. It then delves into the Ukraine Power Grid Attack, a pivotal moment in which cyberattacks on critical infrastructure emerged from the shadows and into the global spotlight. Dragonfly and Triton, each representing the epitome of cyber threats in their own right, are covered in turn to unveil the evolving tactics of adversaries with varying motivations.
The physical mass needed to produce energy from Uranium is much smaller than all other viable sources of energy and it produces way less CO². But what are the drawbacks of this option? Contamination is one of the factors at play, however, Uranium enrichment is also used to produce nuclear bombs. It happens in similar fashion to how benign energy production occurs, making it difficult to discern the two, especially when your only resource is satellite imagery.

- Natanz nuclear facility under construction -NY Times³

### A Brief History of Cyber Attacks

The actual and complete history of cyber attacks against critical infrastructures within the nuclear energy sector would warrant a paper of its own right now, mostly because of how sophisticated the attacks have become over the years but also because they have occurred with some increased frequency since their early days.
Here we will mostly be focusing on the groundbreaking attack that brought attention to the marriage between nuclear energy and cyber security but not before we make memorable mentions that contributed to this devastating attack and to other attacks that followed Stuxnet’s lead in the nuclear sector / cyber security intersection.

### Early Days (2000)

In the early 2000s, cyberattacks on the energy sector were relatively rare, but incidents like the 2000 "ILOVEYOU" virus highlighted key vulnerabilities in computer systems to open a new array of possibilities. Also known as the Love Bug or LoveLetter, this virus was a computer worm that spread rapidly via email in May 2000. It's one of the most notorious malware incidents in the history of the internet.
The ILOVEYOU incident is not directly related to cyberattacks on critical infrastructure in the nuclear energy sector. Instead, it is an early example of a widespread and damaging computer worm that had broader implications for cybersecurity awareness and the potential for cyberattacks to cause widespread disruption. Some of the techniques used here have set the stage for subsequent attacks related to the topic at hand.
Once executed, the virus attempted to overwrite and destroy various types of files, including image files, music files, and document files. It then went on to send copies of itself to all contacts in the victim's Microsoft Outlook address book.
The virus demonstrated the destructive potential of malware and the ease with which it could propagate. It highlighted the vulnerability of computer systems to social engineering attacks, where users were tricked into opening malicious attachments.
This incident played a role in the development of cybersecurity policies and practices, including the use of email filters and increased user education about email attachments.

### Stuxnet (2010)

Stuxnet was a highly sophisticated worm that targeted Iran's nuclear program but inadvertently spread to other countries. It demonstrated the potential for state-sponsored cyberattacks on critical infrastructure, including energy facilities. Up until this point the idea that a computer hack could affect the physical world was far-fetched, but Stuxnet changed this notion completely.
Although Stuxnet was not the first demonstration of such technique, it was the first time it defied the skepticals about the unwanted accessibility of such systems like nuclear power plants.
Stuxnet was discovered in June 2010, though it is believed to have been in the wild for several years before that. It was initially identified by cybersecurity researchers as a highly unusual and complex piece of malware.
Stuxnet exploited a Windows Dynamic Link Library (DLL) file known as "ntoskrnl.exe" (also referred to as ".nlk"), which is not a standard Windows DLL. Instead, it was a cleverly disguised component of the Stuxnet malware designed to compromise Windows operating systems, particularly those used in industrial environments.
The exploit employed a technique known as "DLL injection" to load the malicious code into the memory of the targeted system. In this case, the malware disguised its malicious code as a DLL file named "ntoskrnl.exe" to blend in with legitimate system files.
The choice of "ntoskrnl.exe" was strategic because it is the kernel of the Windows operating system, and thus a critical component. The malware creators hoped that by impersonating such a crucial system file, the malicious code would go unnoticed by security measures and appear as a legitimate part of the Windows OS.
Stuxnet made use of multiple zero-day vulnerabilities (security flaws unknown to the software vendor) to infiltrate Windows systems, including the ".lnk" vulnerability and a vulnerability in the Windows Print Spooler service. The ".lnk" vulnerability allowed Stuxnet to propagate via USB drives, as it could execute code when a user opened a folder containing a malicious shortcut file.

- Windows shortcut icon arrow

Once a system was infected, Stuxnet could propagate itself through various means, including USB drives, network shares, and exploiting vulnerabilities on other systems. Its worm-like characteristics enabled it to move stealthily within networks, infecting Siemens PLCs and other systems within industrial environments.
Stuxnet's ability to exploit a fake "ntoskrnl.exe" DLL and various zero-day vulnerabilities made it a highly sophisticated and targeted malware designed specifically for sabotaging industrial control systems, with a particular focus on Siemens PLCs. This level of sophistication and specificity is what made Stuxnet a groundbreaking cyberweapon and a pivotal event in the history of cybersecurity.

- Siemens S7 300 & S7 400 PLCs

Stuxnet was designed to specifically target Supervisory Control and Data Acquisition (SCADA) systems, particularly those used in Iran's uranium enrichment facilities. Its primary target was the centrifuges used in the enrichment process with the main objective of sabotaging the centrifuges by altering their operational parameters, causing physical damage to the equipment. This was a significant departure from typical malware, which focuses on data theft or disruption.

- Schematic of a Typical Uranium Enrichment Gaseous Centrifuge

Stuxnet is widely believed to be a product of a nation-state-sponsored cyberattack. While no government officially claimed responsibility, it is widely attributed to a joint effort between the United States and Israel with possible collaborations from the United Kingdom and Germany. It is considered a groundbreaking example of a cyberweapon that caused physical damage to critical infrastructure. It demonstrated the potential for cyberattacks to have real-world, kinetic effects.
Its successful targeting of industrial control systems raised concerns about the security of critical infrastructure worldwide, including power plants, water treatment facilities, and more.
The discovery of Stuxnet sparked international discussions about the ethics and legality of state-sponsored cyberattacks and the need for international norms and agreements in cyberspace.
During the events that surrounded Stuxnet’s discovery, researchers poured over the code for months trying to identify its methodologies and intentions around the clock and around the world. The more they uncovered the more baffling it became, forcing the researchers to make difficult ethical decisions along the way, especially about when and how to disclose their findings. All the while already anticipating the future ramifications of such an attack.
Once the the code was reverse-engineered and its intentions officially disclosed to the world the term ‘Cyber Warfare’ became a reality and eventually all centrifuges at Natanz nuclear plant were brought to a halt so the software in the PLCs and their respective SCADA systems could be cleaned up. Stuxnet had achieved its goal. 
Iran never released copies of the malware that infected their plants nor the specific configurations of their PLCs (which Stuxnet was supposedly so keenly seeking) so, although the extensive research and findings point to the Natanz Uranium enrichment plant in Iran, there’s no official confirmation that this was the case.

    “When asked about the role the United States might have played in Stuxnet, 
    Gary Samore, Obama’s chief adviser on weapons of mass destruction and arms 
    control, simply smiled at a Times reporter and said, “I’m glad to hear they 
    are having troubles with their centrifuge machines, and the US and its allies 
    are doing everything we can to make it more complicated” ”

    - Countdown to Zero Day¹

The main concern of researchers was that further attacks would follow using similar methodologies from Stuxnet. However, shortly after the full exposure and containment of Stuxnet, leading Iranian researchers in the nuclear field were attacked on the streets by motorcycle drive-bys gluing bombs to their cars, killing one of them and injuring another alongside passengers in the car at the time.
This came as a further scare tactic for researchers in the field operating in Iran and drove home the point that Stuxnet was trying to make.

### Ukraine Power Grid Attack (2015 and 2016)
Ukraine is no stranger to nuclear incidents. The Chernobyl disaster, which occurred on April 26, 1986, is considered one of the worst nuclear accidents in history. It took place at the Chernobyl Nuclear Power Plant located near the town of Pripyat in the Ukrainian SSR, which was part of the Soviet Union at the time.

    “The former Soviet republic of Ukraine has been a trouble-spot since early 2014, 
    which saw the 'Euromaidan' revolution in support of closer EU integration, 
    the Russian annexation of Crimea and the start of the ongoing pro-Russian 
    separatist insurgency.”

    - ZNET introduction to the attacks⁴

The political scenario was loaded with tension, not akin from Stuxnet’s environment. Taking stage in a country that relies significantly on nuclear power for electricity generation, was a disaster waiting to happen. 
In 2015 and 2016, Ukraine experienced two separate cyberattacks on its power grid. The attackers used malware to disrupt power distribution, leaving hundreds of thousands of people without electricity. The 2015 attack was particularly notable as it marked one of the first known instances of a cyberattack causing a large-scale power outage.
The first attack occurred on December 23, 2015, and resulted in a blackout affecting the Ivano-Frankivsk region in western Ukraine.

- Ivano-Frankivsk region in western Ukraine

Attackers used a variant of the BlackEnergy malware and a custom-built malware tool known as KillDisk. They gained access to the utility's network through spear-phishing emails and used malware to manipulate control systems and disrupt power distribution.
The attack left around 230,000 people without electricity for several hours during the winter. The outage was relatively short-lived, thanks to manual interventions by the utility's operators.
The second attack took place on December 17, 2016, affecting a broader area, including the capital, Kiev. Similar to the 2015 attack, the 2016 attack involved spear-phishing and malware to gain access to the power grid's control systems.
This attack was more widespread and lasted longer, with some areas experiencing power outages for several hours. The attackers also used KillDisk to wipe data from affected systems, making the recovery process more challenging.
Ukrainian authorities and cybersecurity experts attributed the attacks to a Russian state-sponsored group known as SandWorm Team. Russia denied involvement.

### Dragonfly (2017)
The Dragonfly cyber-espionage campaign, also known as Energetic Bear, is a notable example of a sophisticated and targeted campaign that aimed to compromise energy sector infrastructure. The Dragonfly campaign was first discovered and publicly disclosed by cybersecurity researchers in 2014. However, it became more widely known in 2017 when additional details emerged.
The primary targets of the Dragonfly campaign were energy sector organizations, including utility companies, power grid operators, and industrial control system (ICS) vendors. The campaign employed various tactics, techniques, and procedures (TTPs) to compromise targeted organizations including spear-phishing emails, watering hole attacks (compromising websites likely to be visited by targeted personnel), and Trojan malware.
One of Dragonfly's primary methods of infiltration was sending carefully crafted spear-phishing emails to employees within the targeted organizations. Once inside the targeted networks, Dragonfly used remote access trojans to gain control over systems and collect sensitive information.
While attribution is challenging in the world of cyber-espionage, some experts and government agencies suspected that Dragonfly had connections to state-sponsored actors. Russia has been mentioned as a potential origin.

    “In their latest campaign, Dragonfly successfuly “trojanised” legitimate 
    industrial control system (ICS) software. To do so, they first compromised 
    the websites of the ICS software suppliers and replaced legitimate files in 
    their repositories with with their own malware infected versions.”
    
    - ncsc.gov.uk⁵

The objectives of this Dragonfly campaign are believed to have been primarily focused on gathering intelligence about energy infrastructure. This could include information about power generation and distribution systems, which could be valuable for future cyberattacks or espionage.
While no destructive attacks have been attributed to Dragonfly, the potential for disruption or sabotage of critical energy infrastructure was a significant concern.

### TRISIS/Triton (2017)
TRISIS, also known as Triton, is a highly sophisticated computer virus that was designed to target industrial control systems (ICS) and supervisory control and data acquisition (SCADA) systems, specifically those used in critical infrastructure like power plants and chemical facilities. The malware was discovered in 2017, and it is believed to be the work of a nation-state actor with the intent to disrupt or gain control over critical infrastructure. TRISIS/Triton is particularly notorious because it targeted safety systems, which are designed to shut down a facility in the event of a dangerous situation, putting lives and the environment at risk.
The TRISIS (or Triton) malware was discovered targeting a Saudi Arabian petrochemical plant. The attackers likely gained initial access to the target network through traditional methods like phishing or spear-phishing attacks, although specific details of the initial access vector remain undisclosed. Once inside the network, the attackers pivoted to the safety instrumented systems, which control and monitor critical processes.
Like Stuxnet is to the Siemens S7 300/400 PLCs, Triton is also a custom-made malware specifically engineered to target Schneider Electric's Triconex safety instrumented system controllers. This system is widely used in the industrial sector for safety-critical functions. Triton allows attackers to gain remote access to the compromised safety systems, providing them with the ability to override or manipulate safety measures.
Triton is also known for its ability to evade detection and analysis. It can employ anti-forensic techniques to make it challenging for security teams to investigate and analyze its activities. For example hide its code within legitimate files or use encryption to obfuscate its communications.
The incident underscored the importance of robust cybersecurity measures for critical infrastructure and the need for ongoing vigilance against advanced threats and led to increased awareness and collaboration between governments, industry, and cybersecurity experts to strengthen the security of critical infrastructure.

### Key Historical Takeaways
Much like other major technological fields, nuclear energy also has a lack of security awareness and adherence to current standard security practices leaving a collection of important considerations aside either in favor of other interests or genuinely not knowing any better.
Human technical debt in the context of securing advanced applications like nuclear plants refers to the accumulated shortcomings, inefficiencies, or vulnerabilities in the security measures and practices over time. It arises due to a combination of factors, including outdated technology, legacy systems, inadequate risk assessments, and complacency in the face of evolving threats. Some examples include, but are not limited to:
- Legacy Systems: Nuclear plants, like many critical infrastructure facilities, often have legacy systems that were designed and implemented many years ago. These systems may lack modern security features, making them susceptible to cyberattacks.
- Inadequate Updates: Failing to keep software and hardware up to date can create technical debt. This is especially problematic when critical security patches are not applied promptly, leaving vulnerabilities open to exploitation.
- Regulatory Compliance: Compliance with security regulations and standards can become a checkbox exercise rather than a robust security strategy. Organizations may focus on meeting minimum requirements rather than proactively enhancing security.
- Lack of Security Culture: Sometimes, organizations may have a culture that does not prioritize security as a core value. Employees may not be adequately trained or may not be aware of the potential risks.
- Shortcuts and Quick Fixes: Over time, in the face of resource constraints or tight deadlines, organizations might take shortcuts or apply quick fixes that compromise security. These temporary solutions can accumulate and become sources of technical debt.
- Insufficient Risk Assessment: Failure to conduct thorough and up-to-date risk assessments can result in a lack of understanding of the evolving threat landscape and the vulnerabilities within the system.
- Inadequate Budget Allocation: A lack of budget allocation for security can lead to insufficient investment in technology, training, and personnel needed to secure advanced applications effectively.
- Lack of Expertise: Securing advanced applications like nuclear plants requires specialized knowledge and expertise. A shortage of qualified cybersecurity professionals can lead to vulnerabilities going unaddressed.
- Complacency: Once an organization has operated without major incidents for an extended period, there may be a sense of complacency regarding security, leading to neglect and overlooking potential risks.

Addressing human technical debt in securing advanced applications like nuclear plants is essential to minimize risks and ensure the safety and integrity of these critical facilities. This can be achieved through strategies such as:
- Regular security assessments and audits.
- Continuous monitoring and threat intelligence gathering.
- Investing in advanced cybersecurity solutions.
- Training and awareness programs for staff.
- Prioritizing security in the development and maintenance of systems.
- Keeping abreast of evolving security regulations and standards.
- Proactive risk management and mitigation strategies.

Technical debt is not the only reason these attacks are made possible but here the gap that needs to be covered is vast. Considering how advanced the technologies that need to be secured are, their protective counter-parts need to follow suit, especially as they’ve evolved to become indispensable support to the daily needs of human beings.

### References:
1) [Countdown to Zero Day - Kim Zetter](https://www.penguinrandomhouse.com/books/219931/countdown-to-zero-day-by-kim-zetter/)
2) https://www-nds.iaea.org/
3) https://www.nytimes.com/2020/12/09/world/natanz-nuclear-facility-iran.html
4) https://www.zdnet.com/article/how-hackers-attacked-ukraines-power-grid-implications-for-industrial-iot-security/
5) https://www.ncsc.gov.uk/collection/supply-chain-security/third-party-software-providers

### Other Notable Mentions:
- https://en.wikipedia.org/wiki/2015_Ukraine_power_grid_hack
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/dragonfly-energy-companies-sabotage
- [Sandworm - Andy Greenberg](https://www.penguinrandomhouse.com/books/597684/sandworm-by-andy-greenberg/)
