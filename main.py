from simulator import Processor


run = Processor()
run.load_mc()

while True:

    run.fetch()
    # print(run._IR)

    if run._IR == '0'*8:
        break
    run.decode()
    # print(run._currOperationId)
    run.execute()
    run.memoryAccess()
    run.registerUpdate()
    # run._registerFile.print_registers()

run._PMI.print_memory()
print("Data in output.txt printed")
run.printData()
run.print_registers_in_a_file(run)
