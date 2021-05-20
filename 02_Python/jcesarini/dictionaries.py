monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dic": "December",
}
print(monthConversions["Nov"])
print(monthConversions.get("Apr"))
print(monthConversions.get("Nob","Not a valid key"))