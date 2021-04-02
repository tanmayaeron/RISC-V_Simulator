from simulator import Processor


run = Processor()
run.load_mc("fib.mc")

while True:
    run.fetch()
    if run.getIR() == '0'*8:
        break
    run.decode()
    run.execute()
    run.memoryAccess()
    run.registerUpdate()
    

run.printRegisters()
run.printData()
