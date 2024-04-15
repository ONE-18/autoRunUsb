import subprocess

def readImput():
    try:
        ret = []
        with open('input.txt', 'r') as f:
            data = f.read().splitlines()
            if len(data) == 0:
                print('File is empty')
                return None
            for l in data:
                if l.startswith('#'):
                    continue
                else:
                    l = l.split('|')
                    if len(l) == 2:
                        ret.append(l)
                    else:
                        print('Invalid line:', l)
            return ret
    except FileNotFoundError:
        print('File not found')
        with open('input.txt', 'w') as f:
            f.write('# This is the input file\n')
            f.write('# Format: <key>:<value>\n')
        return None
    except Exception as e:
        print('Error reading file:', e)
        return None

def check_for_USB(letra):
    output = subprocess.check_output("wmic logicaldisk get caption, drivetype", shell=True)
    data = str(output)
    if (letra+':') in data:
        return True
    else:
        return False
    
if __name__ == '__main__':
    tasks = readImput()
    while tasks is not None:
        for t in tasks:
            if check_for_USB(t[0]):
                print('USB found:', t[0])
                try:
                    subprocess.Popen(['start', 'cmd', '/k', t[1]], shell=True)
                except:
                    print('Error')
                tasks.remove(t)
            # else:
            #     print('USB not found:', t[0])
        
        if len(tasks) == 0:
            print('All tasks completed')
            break