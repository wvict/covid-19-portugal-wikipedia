import sample.report as report
import sample.date as date
import sample.format as format
import pandas as pd


def summary_table(summary, symptoms):
    print('Generating Summary table...')

    #adding comma formatting to numbers in results array
    for k,v in summary.items(): 
        summary[k] = format.add_commas(v)

    link = report.info()['link']
    date_summary = format.date_symptom(report.info()['report_date'])
 
    
    f = open('output/SummaryTable.txt', 'w+')
    result="""== Summary ==
{| class="wikitable" 
|+COVID-19
! colspan="2" |Cases ["""+link+""" """+report.info()['report_date']+"""]
|-
!total confirmed cases
|"""+summary['confirmed_cases']+"""
|-
!total not confirmed cases 
|"""+summary['not_confirmed_cases']+"""
|-
!total suspected cases (since 1 January 2020)
|"""+summary['suspected_cases']+"""
|-
!under surveillance
|"""+summary['under_surveillance']+"""
|-
!waiting for results
|"""+summary['waiting_results']+"""
|-
!recovered
|"""+summary['recovered']+"""
|-
!deaths
|"""+summary['deaths']+"""
|-
|}\n"""

    #Symptoms occurrence table

    percentages = symptoms['percentages']
    occurrence = symptoms['occurrence']#whatch out for {{}} problems while using string literals in python
    result += """
{| {{Table}} 
!   !! high fever !! dry cough !! difficult breathing !! headache !! muscular pain !! tiredness
|-
! % of cases with symptoms
| """+percentages[0]+"""
| """+percentages[1]+"""
| """+percentages[2]+"""
| """+percentages[3]+"""
| """+percentages[4]+"""
| """+percentages[5]+"""
|-
|}
There was only reported information regarding the occurrence of symptoms on """+occurrence+""" of confirmed cases.<ref>{{cite web|url="""+link+""" |title=COVID-19 RELATÓRIO DE SITUAÇÃO |date="""+date_summary+""" |website=covid19.min-saude.pt}}</ref>"""
    
    f.write(result)
    f.close()


def age_and_gender_graphs(cases, deaths):
    print('Generating cases by age and gender graphs...')
    cases_men = cases['men']
    cases_women = cases['women']

    deaths_men = deaths['men']
    deaths_women = deaths['women']

    result = """=== Cases by age and gender ===
{{Graph:Chart
|width=320
|colors=blue,orange
|showValues=
|xAxisTitle=Age
|xAxisAngle=-50
|type=rect
|x= 0-9, 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80+ 
|yAxisTitle=No. of cases
|legend=Legend
|y1= """+cases_men+"""
|y2= """+cases_women+"""
|y1Title=Men
|y2Title=Women
|yGrid= |xGrid=
}}
<br>
{{Graph:Chart
|width=320
|colors=blue,orange
|showValues=
|xAxisTitle=Age
|xAxisAngle=-50
|type=rect
|x= 0-9, 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80+ 
|yAxisTitle=No. of deaths
|legend=Legend
|y1="""+deaths_men+"""
|y2= """+deaths_women+"""
|y1Title=Men
|y2Title=Women
|yGrid= |xGrid=
}}"""
    f = open('output/GraphsCasesByAgeAndGender.txt', 'w+')
    f.write(result)
    f.close()

def timeline_graphs():
    print('Generating timeline graphs...')
    df = pd.read_csv('portugal_data.csv')
    columns = list(df.columns)
    date = [format.date_timeline(i) for i in list(df.date)]
    data = {}
    for i in columns:
        if i=='date':
            data[i] = format.data_for_timeline(date)
        else:
            data[i] = format.data_for_timeline(list(df[i]))

    result = """=== Timeline graphs ===
<!-- Cumulative Cases per day -->
{{Graph:Chart
|type=line
|linewidth=1
|showSymbols=1
|width=700
|colors=#F46D43,#A50026,#C4ADA0,#C4ADB0,#C4ADC0
|showValues=
|xAxisTitle=Date
|xAxisAngle=-40
|x= """+data['date']+"""
|yAxisTitle=No. of cases
|legend=Legend
|y1= """+data['total_cases']+"""
|y1Title=Total confirmed cases
|yGrid= |xGrid=
}}

<!-- Cases per day -->

{{Graph:Chart
|width=700
|colors=#F46D43
|showValues=
|xAxisTitle=Date
|xAxisAngle=-40
|type=rect
|x= """+data['date']+"""
|yAxisTitle=New cases
|legend=Legend
|y1= """+data['daily_cases']+"""
|y1Title=New cases per day
|yGrid= |xGrid=
}}
<br />

<!-- Cumulative Deaths and Recoveries per day -->

{{Graph:Chart
|type=line
|linewidth=1
|showSymbols=1
|width=700
|colors=#A50026,SkyBlue,#FF0000
|showValues=
|xAxisTitle=Date
|xAxisAngle=-40
|x= """+data['date']+"""
|yAxisTitle=No. of cases
|legend=Legend
|y1Title=Total confirmed deaths
|y1= """+data['total_deaths']+"""
|y2Title=Total confirmed recoveries
|y2= """+data['recovered']+"""
|yGrid= |xGrid=
}}
<br />

<!-- Hospital admitted cases -->

{{Graph:Chart
|type=line
|linewidth=1
|showSymbols=1
|width=700
|colors=red, #FF4080
|showValues=
|xAxisTitle=Date
|xAxisAngle=-40
|x= """+data['date']+"""
|yAxisTitle=No. of cases
|legend=Legend
|y1Title=ICU
|y1= """+data['hospital_icu']+"""
|y2Title=Stable
|y2= """+data['hospital_stable']+"""
|yGrid= |xGrid=
}}
<br />

<!-- ICU Variation -->

{{Graph:Chart
|width=700
|colors=#FF0000
|showValues=offset:2
|xAxisTitle=Date
|xAxisAngle=-40
|type=rect
|x= """+data['date']+"""
|yAxisTitle=Cases in ICU variation
|legend=Legend
|y1= """+data['icu_variation']+"""
|y1Title = Cases in ICU variation per day
|yGrid= |xGrid= 
}}

<!-- Deaths per day -->

{{Graph:Chart
|width=700
|colors=black
|showValues=
|xAxisTitle=Date
|xAxisAngle=-40
|type=rect
|x= """+data['date']+"""
|yAxisTitle=New deaths
|legend=Legend
|y1=  """+data['daily_deaths']+"""
|y1Title=New deaths per day
|yGrid= |xGrid=
}}
<br />

{{clear}}

"""
    with open('output/TimelineGraphs.txt', 'w+') as f:
        f.write(result)
    
