from CLass_Offline import Offline

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def integrationsTest_af_Offline_Start():
    offLineSpiller = Offline()
    return offLineSpiller.spilModComputer()

def integrationsTest_af_Online_Start():
    return False





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Integrations tests for slagskibsspillet")
    #Her testes om alle integrationer er korrekte
    if integrationsTest_af_Offline_Start():
        print("integrationsTest_af_Offline_Start udført korrekt")
    else:
        print("integrationsTest_af_Offline_Start fejler")

    if integrationsTest_af_Online_Start():
        print("integrationsTest_af_Online_Start udført korrekt")
    else:
        print("integrationsTest_af_Online_Start fejler")




