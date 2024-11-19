import utils
import read_csv
import charts

#print(keys, values)


def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda cont: cont['Continent'] == 'South America', data))
  #list_porcentage = list(map(lambda porc: porc['World Population Percentage'], data))
  #list_countrys = list(map(lambda country: country['Country/Territory'], data))
  
  countrys = utils.popul_countrys(data)
  percentages = utils.popul_perce(data)

  #print(countrys, percentages)

  charts.generate_pie_chart(countrys, percentages)
  
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()
