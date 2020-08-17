class MatrixCalc:    
    def __init__(self):
        self.main_acts = {
            '1':['. Add matrices', self.add_matrix],
            '2':['. Multiply matrix by a constant', self.const_mult_matrix],
            '3':['. Multiply matrices', self.mult_matrix],
            '4':['. Transpose matrix', self.init_transpose],
            '5':['. Calculate a determinant', self.calc_det],
            '0':['. Exit', False]}

        self.transpose_acts = {
            '1':['. Main diagonal', self.transpose_main_diagonal],
            '2':['. Side diagonal', self.transpose_side_diagonal],
            '3':['. Vertical line', self.transpose_vertical_line],
            '4':['. Horizontal line', self.transpose_horizontal_line]}

    def start(self):
        self.print_acts(self.main_acts)

        action = input('Your choice: ')
        while self.main_acts[action][1]:
            self.main_acts[action][1]()
            print()
            self.print_acts(self.main_acts)
            action = input('Your choice: ')

    def print_acts(self, acts):
        for key in acts.keys():
            print(key, acts[key][0], sep='')

    def input_data(self, order=['first', 'second'], is_const=False):
        data = []
        
        for i in order:
            size = input(f'Enter size of {i} matrix: ').split()
            print(f'Enter {i} matrix: ')
            M = [list(map(float, input().split())) for _ in range(int(size[0]))]
            data.append(M)
        
        if is_const:
            const = float(input('Enter constant: '))
            data.append(const)
        
        return data

    def add_matrix(self):
        M1, M2 = self.input_data()
        
        size_1 = [len(M1), len(M1[0])]
        size_2 = [len(M2), len(M2[0])]
        
        if size_1 == size_2:
            print('The result is:')
            for rows in zip(M1, M2):
                print(*[sum(x) for x in zip(*rows)])
        else:
            print('The operation cannot be performed.')


    def const_mult_matrix(self):
        M, const = self.input_data(order=[''], is_const=True)
        
        print('The result is:')
        for row in M:
            print(*[cell * const for cell in row])

    def mult_matrix(self):
        M1, M2 = self.input_data()
        
        if len(M1[0]) == len(M2):
            M2 = list(zip(*M2))
            
            print('The result is:')
            for row1 in M1:
                print(*[sum(list(map(lambda x, y: x * y, row1, row2))) for row2 in M2])
        else:
            print('The operation cannot be performed.')

    def init_transpose(self):
        self.print_acts(self.transpose_acts)
        
        action = input('Your choice: ')
        self.transpose_acts[action][1]()
    
    def transpose_main_diagonal(self):
        M = self.input_data([''])[0]
        
        M = list(zip(*M))
        print('The result is:')
        for row in M:
            print(*[cell for cell in row])

    def transpose_side_diagonal(self):
        M = self.input_data([''])[0]
        
        M = list(zip(*M))
        print('The result is:')
        for row in reversed(M):
            print(*[cell for cell in reversed(row)])

    def transpose_vertical_line(self):
        M = self.input_data([''])[0]
        
        print('The result is:')
        for row in M:
            print(*[cell for cell in reversed(row)])

    def transpose_horizontal_line(self):
        M = self.input_data([''])[0]
        
        print('The result is:')
        for row in reversed(M):
            print(*[cell for cell in row])
    
    def calc_det(self):
        M = self.input_data([''])[0]
        
        n = len(M)
        for d_e in range(n):
            
            if M[d_e][d_e] == 0:
                for rest in range(d_e+1, n):
                    if M[d_e][rest] != 0:
                        for na_col in range(n):
                            M[na_col][d_e] = M[na_col][d_e] + M[na_col][rest]
                        break
                    elif M[rest][d_e] != 0:
                        for na_row in range(n):
                            M[d_e][na_row] = M[d_e][na_row] + M[rest][na_row]
                        break
            
            for null_col in range(d_e+1, n):
                null_coef = M[null_col][d_e] / M[d_e][d_e]
                
                for change in range(n):
                    M[null_col][change] = M[null_col][change] - null_coef * M[d_e][change]
        
        result = 1
        
        for d_elem in range(n):
            result *= M[d_elem][d_elem]
        
        print(result)
                        

matrix_calc = MatrixCalc()
matrix_calc.start()
