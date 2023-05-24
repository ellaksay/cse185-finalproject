setup(
  name='PET',
  version=VERSION, 
  Description='CSE 185 PET Project', 
  authors='Brianna Sanchez, Ella Say, Anu Selvaraj',
  pacakages=find_packages(),
  entry_points={
    "console_scripts": {
        "pet=pet.pet:main"
    },
  },
)
