from fpdf import FPDF

# Créer un PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Titre
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Roadmap : Devenir Expert en Analyse Blockchain", ln=True, align="C")
pdf.ln(10)

# Contenu du PDF
content = """
🎯 Objectif : Devenir capable de lire, comprendre et produire des analyses on-chain (type Dune, Arkham, Nansen)

PHASE 1 : Bases de l’analyse on-chain (7 à 10 jours)
----------------------------------------------------
Objectifs :
- Lire une transaction sur Etherscan
- Comprendre logs / events
- Analyser une adresse publique

Actions :
1. Explorer 3 transactions sur etherscan.io
2. Lire la doc d’Etherscan : https://docs.etherscan.io
3. Analyser une adresse sur DeBank ou Arkham

PHASE 2 : Dune + SQL (2 semaines)
---------------------------------
Objectifs :
- Apprendre à extraire et visualiser les données on-chain

Actions :
1. Créer un compte Dune : https://dune.com
2. Suivre le tutoriel : https://dune.com/tutorial
3. Apprendre SQL : https://sqlbolt.com (focus SELECT, JOIN, GROUP BY)

PHASE 3 : Premier Dashboard (1-2 semaines)
------------------------------------------
Objectif :
- Créer une analyse visuelle, la publier et te faire remarquer

Exemples de projets :
- Volume quotidien de swaps Uniswap
- Transactions sur Aave ou Curve
- Suivi de la TVL

Publication recommandée : thread sur Twitter/X

PHASE 4 : Approfondissement (long terme)
----------------------------------------
Choisir une spécialisation :
- DeFi Analyst (Uniswap, Curve…)
- Hacker Tracker (analyse de hacks)
- Whale Watcher (comportement des gros portefeuilles)
- Data Scientist Web3 (Python + data viz)

Prochaines étapes :
- Solidity : https://solidity-by-example.org/
- Python : cours YouTube "Python for Data Science freeCodeCamp"
- Rejoindre les communautés : Dune, Flipside, Arkham

PLAN D’ACTION : 3 prochains jours
----------------------------------
Jour 1 : Lire 3 transactions sur Etherscan (1h)
Jour 2 : Créer compte Dune + faire le tuto (1-2h)
Jour 3 : 3 leçons SQL sur SQLBolt (1h)
"""

# Ajouter le contenu ligne par ligne
for line in content.strip().split('\n'):
    pdf.multi_cell(0, 10, line)

# Enregistrer le PDF
pdf.output("Roadmap_Expert_Analyse_Blockchain.pdf")
