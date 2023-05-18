
def page_title(info:str)-> str:
    if info == 'en':
        return 'Profile | Marcelo Peres'
    elif info == 'pt':
        return 'Perfil | Marcelo Peres'
    else:
        None

page_icon = ':wave:'
name = 'Marcelo Peres'


def role(info:str)-> str:
    if info == 'en':
        return 'Data Engineer & Analyst Professional'
    elif info == 'pt':
        return 'Engenheiro & Analista de Dados'
    else:
        None

info = '''\n
* - Git-lab-hub | CI/CD--Jenkins/Gitlab | Terraform
* - GCP--AWS | Storage | Athena/Redshift/Bigquery
* - ETL--ELT | Lambda/G functions/glue jobs/Datastage
* - Airflow | Sap | Oracle | API.
'''
email = 'brmarcelo.peres@gmail.com'
social_media = {
    'LinkedIn': 'https://www.linkedin.com/in/marcelo-peres-24611928/',
    'GitHub': 'https://github.com/Marcelo-Peres'
}


def qualification(info:str)-> str:
    if info == 'en':
        return '## Experience & Qualifications'
    elif info == 'pt':
        return '## Experiências & Qualificações'
    else:
        None


def qualification_info(info:str)-> str:
    if info == 'en':
        return '''
- ✔️ 8 Years of experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python, Excel and SQL
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
'''
    elif info == 'pt':
        return '''
- ✔️ 8 anos de experiência extraindo informações relevantes de fontes de diversas
- ✔️ Sólida experiência e conhecimento em Python, Excel and SQL
- ✔️ Bom entendimento dos princípios da estatística e suas aplicações
- ✔️ Excelente comuinicação entre os vários níveis da empresa
'''
    else:
        None


def skill(info:str)-> str:
    if info == 'en':
        return '## Hard Skills'
    elif info == 'pt':
        return '## Habilidades Sólidas'
    else:
        None


def skill_info(info:str)-> str:
    if info == 'en':
        return '''
- 👩‍💻 Programming: Python (Pandas), SQL, Pyspark & Spark
- 📊 Data Visulization: Power BI, Tableau, Plotly
- 🗄️ Databases: Postgres, MySQL, SQL-Server & Oracle
'''
    elif info == 'pt':
        return '''
- 👩‍💻 Programação: Python (Pandas), SQL, Pyspark & Spark
- 📊 Visualização de Dados: Power BI, Tableau, Plotly
- 🗄️ Banco de Dados: Postgres, MySQL, SQL-Server & Oracle
'''
    else:
        None


def job_header(info:str)-> str:
    if info == 'en':
        return '## Work Experience'
    elif info == 'pt':
        return '## Experiências em Empresas'
    else:
        None


def job_t03(info:str)-> str:
    if info == 'en':
        return '#### 🚧 Data Engineer | A3Data'
    elif info == 'pt':
        return '#### 🚧 Engenheiro de Dados | A3Data'
    else:
        None


def job_t03_time(info:str)-> str:
    if info == 'en':
        return '##### Dec 2022 - Mar 2023 | 04 months'
    elif info == 'pt':
        return '##### Dez 2022 - Mar 2023 | 04 mmeses'
    else:
        None


def job_t03_info(info:str)-> str:
    if info == 'en':
        return '''<div style="text-align: justify;">
GCP - Google Cloud Platform\n
Stellantis - Datalake project

Responsible for creating tools to interect data at plataform.

- ► Tools used:
    * ✔️ Terraform;
    * ✔️ Google Storage;
    * ✔️ BigQuery;
    * ✔️ Google Functions;
    * ✔️ Airflow;
    * ✔️ Python;
    * ✔️ SQL.
'''
    elif info == 'pt':
        return '''<div style="text-align: justify;">
GCP - Google Cloud Platform\n
Stellantis - Projeto Datalake

Responsável por criar ferramentas de interação na Plataforma

- ► Ferramentas usadas:
    * ✔️ Terraform;
    * ✔️ Google Storage;
    * ✔️ BigQuery;
    * ✔️ Google Functions;
    * ✔️ Airflow;
    * ✔️ Python;
    * ✔️ SQL.
'''
    else:
        None


def job_t02(info:str)-> str:
    if info == 'en':
        return '#### 🚧 Data Engineer Consultant | Via Consulting'
    if info == 'pt':
        return '#### 🚧 Consultor Engenheiro de Dados | Via Consulting'
    else:
        None


def job_t02_time(info:str)-> str:
    if info == 'en':
        return '##### Apr 2022 - Sep 2022 | 06 months'
    elif info == 'pt':
        return '##### Abr 2022 - Set 2022 | 06 meses'
    else:
        None


def job_t02_info(info:str)-> str:
    if info == 'en':
        return '''<div style="text-align: justify;">\n
###### Via Consulting - Project - Zendesk Replication
* ► Continuous pushing of data in a AWS environment using tools like:
    * ✔️ Pyspark Spark Glue jobs;
    * ✔️ Cloud Formation;
    * ✔️ AWS SQL Athena;
    * ✔️ Apache Hudi metadata for data governance.

###### Unimed Insurance - Project - Stuffed Wallet

* ► Colaborating with the team in a ETL process using tools like:
    * ✔️ informatica Powercenter;
    * ✔️ PLSQL - Oracle.
The idea of the project is a campaign that supports the score of the company's brokers.

###### Smiles S.A. - Project - Gol Spend & Get

* ► AWS Python lambda function that validates a files to be called by an API.
    * << Resources >>:
    * ✔️ Cloud Formation;
    * ✔️ Python with unit tests;
    * ✔️ Github release info;
    * ✔️ Jenkins to observe github uploaded code;
    * ✔️ Sonar for code quality;
    * ✔️ End of Devops stack with deploy.
</div>'''
    elif info == 'pt':
        return '''<div style="text-align: justify;">\n
###### Via Consulting - Projeto - Replicação do Zendesk
* ► Atualização continua de dados no ambiente AWS usando ferramentas como:
    * ✔️ Pyspark Spark Glue jobs;
    * ✔️ Cloud Formation;
    * ✔️ AWS SQL Athena;
    * ✔️ Apache Hudi metadata para governança de dados.

###### Seguros Unimed - Projeto - Carteira Recheada

* ► Colaborando com o time nos ETLs e processos de carga usando:
    * ✔️ informatica Powercenter;
    * ✔️ PLSQL - Oracle.
A ideia do projeto é uma campanha que dá suporte as pontuações dos consultores de vendas.

###### Smiles S.A. - Projeto - Gol Spend & Get

* ► Função lambda da AWS em Python para validar arquivos chamados por outra API.
    * << Recursos >>:
    * ✔️ Cloud Formation;
    * ✔️ Python com unit tests;
    * ✔️ Github informações de release;
    * ✔️ Jenkins para observar github nas atualizações de código;
    * ✔️ Sonar para verificar a qualidade do código;
    * ✔️ Término e deploy da esteira Devops.
</div>'''
    else:
        None


def job_t01(info:str)-> str:
    if info == 'en':
        return '#### 🚧 AWS & BI Consultant | BI4all'
    elif info == 'pt':
        return '#### 🚧 Consultor AWS & BI | BI4all'
    else:
        None


def job_t01_time(info:str)-> str:
    if info == 'en':
        return '##### Jul 2021 - May 2022 | 11 months'
    elif info == 'pt':
        return '##### Jul 2021 - Mai 2022 | 11 meses'
    else:
        None


def job_t01_info(info:str)-> str:
    if info == 'en':
        return '''<div style="text-align: justify;">\n
###### Manserv S/A
* ► AWS Management asset
    * ✔️ Responsible for creating data pipelines to push data in S3 using python AWS lambda funtions.
    * ✔️ Using packages such as awswrangler, xmltodict, json and much more.
    * ✔️ Being involved in great projects with the relevant skills, accessing different APIs from several providers.
    * ✔️ Some of these ones are Volvo, Nuntec, Komatsu - Komtrax, Caterpillar and many others.
    * ✔️ Transforming XML and JSON API extrations into tabular data to be recorded in parquet table format, grating a better use of S3 bucket as much as gaing performance in a compressed file format.
</div>'''
    elif info == 'pt':
        return '''<div style="text-align: justify;">\n
###### Manserv S/A
* ► Gerenciamento AWS
    * ✔️ Responsável por criar pipelines de atualização de dados no bucket S3 AWS usando funções lambda com Python.
    * ✔️ Pacostes utilizados: awswrangler, xmltodict, json entre outros.
    * ✔️ Envolvido em projetos relevantes, tendo habilidades para lidar com diferentes provedores de APIs.
    * ✔️ Provedores de API: Volvo, Nuntec, Komatsu - Komtrax, Caterpillar entre outros.
    * ✔️ Tipos de dados acessados via API: Extrações de XML & JSON transpondo para dados tabulares para posterior gravação no bucket do cliente em arquivos no formato parquet, garantindo melhor performance e uso.
</div>'''
    else:
        None
