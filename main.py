import ifcopenshell
import xlsxwriter

print ('loading the model .....') 
model=ifcopenshell.open('models/Duplex_A_20110907.ifc')

print ('hello IFC - model loaded')

project = (model.by_type('IfcProject'))

print (project[0].LongName) 

#products = model.by_type('IfcProduct')
#for product in products:
    #print(product.is_a())    



window = model.by_type('IfcWindow')[0]
print(window.GlobalId)
print(window.Name)


#window = model.by_type('IfcWindow')[0]
#for definition in window.IsDefinedBy:
    # To support IFC2X3, we need to filter our results.
    #if definition.is_a('IfcRelDefinesByProperties'):
        #property_set = definition.RelatingPropertyDefinition
        #print(property_set.Name) 

workbook = xlsxwriter.Workbook('output/test.xlsx')
answer = input("Want to write excel for the follwing entities? Enter y/n: ") 
if answer == ("y") or answer == ("Y") or answer == ("Yes") or answer == ("yes"): 
def makeASheet(ifcType):
    sheet = workbook.add_worksheet(ifcType)
    # define which row you want to start writing at.
    row =1
    for entity in model.by_type(ifcType):
        # this writes the data to the sheet
        # sheet.write(row, column, data)
        sheet.write(row,0,str(entity.Name))
        # this 'iterates' row so that each time we step down a row.
        # otherwise each new entry would overwrite the previous entry.
        row+=1
# here we can call the function and put it the argument
# in this case we are asking for the results of 
# different IFC entities to be written to their own sheets       
makeASheet('IfcSpace')
makeASheet('IfcWindow')
# it is important to close the workbook afterwards
workbook.close() 