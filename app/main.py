import utils
import read_csv
import charts
import pandas as pd

#print(keys, values)


def run():
  '''
  data = list(filter(lambda cont: cont['Continent'] == 'South America', data))
  #list_porcentage = list(map(lambda porc: porc['World Population Percentage'], data))
  #list_countrys = list(map(lambda country: country['Country/Territory'], data))
  countrys = utils.popul_countrys(data)
  percentages = utils.popul_perce(data)
  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'South America']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)
  
  
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()
