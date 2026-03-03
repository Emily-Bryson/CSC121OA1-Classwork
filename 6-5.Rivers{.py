major_rivers = {
  "Nile":"Egypt",
  "Amazon":"Brazil",
  "Darling":"Australia"  
}
for river,country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("Rivers included:")
for river in major_rivers.keys():
    print(river.title())
print("Countries included:")
for country in major_rivers.values():
    print(country.title())