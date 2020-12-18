class Instruction:
    def __init__(self, line):
        s = line.split(" ")
        self.name = s[0]
        self.amount = int(s[1])
        self.label = ""
        self.delete = False

    def __repr__(self):
        return "<Instruction__%s: %d. Label: %s>" % (self.name, self.amount, self.label)



with open("input.txt", 'r') as f:
    instructions = [Instruction(a) for a in f.readlines()]
    #Generate labels
    for i, a in enumerate(instructions):
        if a.name == "jmp":
            abs_addr = i+a.amount
            while abs_addr < len(instructions) and instructions[abs_addr].name == "nop" :
                abs_addr+=1
            if abs_addr >= len(instructions):
                a.delete = True
                continue
            a.amount = abs_addr
            instructions[abs_addr].label = "label_" + str(abs_addr)
    instructions = [a for a in instructions if a.name != "nop" and not a.delete]
    print('declare i32 @printf(i8*, ...) #1')
    print('@.str = private unnamed_addr constant [4 x i8] c"%d\\0A\\00", align 1')
    print('define i32 @main(){')
    print('\t%a1 = alloca i32')
    print('\tstore i32 0, i32* %a1')
    ip = 2
    for i in instructions:
        if i.label != "":
            print("\tbr label %%%s" % (i.label))
            print("\t%s:" % (i.label))
        if i.name == "acc":
            print('\t%a{} = load i32, i32* %a1'.format(ip))
            print('\t%a{} = add i32 {}, %a{}'.format(ip+1, i.amount, ip))
            print('\tstore i32 %a{}, i32* %a1'.format(ip+1))
            ip += 2
        elif i.name == "jmp":
            print("\tbr label %%label_%s" % (i.amount))
    print('\t%a{} = load i32, i32* %a1'.format(ip))
    print('\tcall i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i64 0, i64 0), i32 %a{})'.format(ip))
    print('\tret i32 0')
    print("}")