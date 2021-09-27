from kit.dependency_file import *



class info_popup:
    
    def show_table(self,arr):
        print(tabulate(arr[0], arr[1], tablefmt=arr[2], showindex="always"))

    def init_info(self):
        table = [ ["search space dimention" , self.ndim],["total population",self.pdim],["child dimention",self.cdim],["mutation dimention",self.mdim],["search shape",tabulate(self.pspace,["min","max"],tablefmt="grid")] ]; 
        arr = [table,["names","#"],"pretty"]
        self.show_table(arr)
        return self
    
    def show_pop(self):
        rows =  [x.values() for x in self.pop]
        print(tabulate(rows,['probability','age','values','evaluation'],tablefmt="pretty", showindex="always"));
        return self;
    
    def show_parents(self):
        rows =  [x.values() for x in self.parents]
        print(tabulate(rows,['probability','age','values','evaluation'],tablefmt="pretty", showindex="always"));
        return self;
    
    def show_childs(self):
        rows =  [x.values() for x in self.child]
        print(tabulate(rows,['probability','age','values','evaluation'],tablefmt="pretty", showindex="always"));
        return self;
    
    def show_mutates(self):
        rows =  [x.values() for x in self.mutation]
        print(tabulate(rows,['probability','age','values','evaluation'],tablefmt="pretty", showindex="always"));
        return self;

    def show_generation(self):
        rows =  [x.values() for x in self.generation]
        print(tabulate(rows,['probability','age','values','evaluation'],tablefmt="pretty", showindex="always"));
        return self;

    def excel_export(self):
        
        wb = Workbook()
        ts = 'workbook'+ str(time.time()) + '.xlsx'
        dest_filename = ts

        ws1 = wb.active
        ws1.title = "population"   
        ws1['A1'] = 'probability';
        ws1['B1'] = 'age';
        ws1['C1'] = 'values';
        ws1['D1'] = 'evaluation';
        row_it = 2;    
        for row in self.pop:
             ws1['A'+str(row_it)] = (row['pr']);
             ws1['B'+str(row_it)] = (row['age']);
             ws1['C'+str(row_it)] = str(row['value']);
             ws1['D'+str(row_it)] = (row['evaluation']);
             row_it += 1
             
        ws2 = wb.create_sheet(title="parents")
        ws2['A1'] = 'probability';
        ws2['B1'] = 'age';
        ws2['C1'] = 'values';
        ws2['D1'] = 'evaluation';
        row_it = 2;    
        for row in self.parents:
             ws2['A'+str(row_it)] = (row['pr']);
             ws2['B'+str(row_it)] = (row['age']);
             ws2['C'+str(row_it)] = str(row['value']);
             ws2['D'+str(row_it)] = (row['evaluation']);
             row_it += 1

        ws3 = wb.create_sheet(title="childs")
        ws3['A1'] = 'probability';
        ws3['B1'] = 'age';
        ws3['C1'] = 'values';
        ws3['D1'] = 'evaluation';
        row_it = 2;    
        for row in self.child:
             ws3['A'+str(row_it)] = (row['pr']);
             ws3['B'+str(row_it)] = (row['age']);
             ws3['C'+str(row_it)] = str(row['value']);
             ws3['D'+str(row_it)] = (row['evaluation']);
             row_it += 1
             
        ws4 = wb.create_sheet(title="mutation")
        ws4['A1'] = 'probability';
        ws4['B1'] = 'age';
        ws4['C1'] = 'values';
        ws4['D1'] = 'evaluation';
        row_it = 2;    
        for row in self.mutation:
             ws4['A'+str(row_it)] = (row['pr']);
             ws4['B'+str(row_it)] = (row['age']);
             ws4['C'+str(row_it)] = str(row['value']);
             ws4['D'+str(row_it)] = (row['evaluation']);
             row_it += 1

        ws5 = wb.create_sheet(title="generation")
        ws5['A1'] = 'probability';
        ws5['B1'] = 'age';
        ws5['C1'] = 'values';
        ws5['D1'] = 'evaluation';
        row_it = 2;    
        for row in self.generation:
             ws5['A'+str(row_it)] = (row['pr']);
             ws5['B'+str(row_it)] = (row['age']);
             ws5['C'+str(row_it)] = str(row['value']);
             ws5['D'+str(row_it)] = (row['evaluation']);
             row_it += 1


        
        wb.save(filename = dest_filename)
        return self
