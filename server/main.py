import os
import zipfile
import glob
import shutil

source_path = '../source/*'
destinatin_path = '../destination'
server_path = './All_file.zip'
add_postfix = [1,2,3]

while True:

        source_objec = glob.glob(source_path)

        source_object =[]
        for s_b in source_objec:
            if s_b.endswith('.txt'):
                source_object.append(s_b)

        if len(source_object)>0:
            object_path = source_object[0]
            shutil.copy(object_path,'.')
            object_name = object_path.split('\\')[-1].split('.')

            prefix = object_name[0]
            postfix = object_name[1]

        try:
            for item in range(len(add_postfix)):
                file_name = prefix+'_'+str(item+1)+'.'+postfix+' will have '+str((item+1)*10)+ ' lines'
                shutil.copy(object_path,f'./{file_name}')

            handle = zipfile.ZipFile('All_file.zip','w')
            for x in os.listdir():
                if x.endswith('lines'):
                    handle.write(x,compress_type=zipfile.ZIP_DEFLATED)

            handle.close()

            shutil.move(server_path,destinatin_path)
            targer = '../destination/All_file.zip'
            handle = zipfile.ZipFile(targer,'r')
            handle.extractall('../destination/')          
            handle.close()
        
        except Exception as e:
            # print('Oh, bad!')
            print(f'Catch error is:-> {e}')

        for x in os.listdir():
            if x.endswith('lines'):
                os.remove(x)


        try:
            os.remove('../destination/All_file.zip')
            os.remove(object_path)
            os.remove(object_path.split('\\')[-1])
            # os.remove('./All_file.zip')
        except FileNotFoundError as e:
            break
           
        finally:
            source__pat ='../source/*'
            s = glob.glob(source__pat)
            
            def run(runfile):
                with open(runfile,"r") as rnf:
                    exec(rnf.read())
            for x in  s:
                try:
                    if x.endswith('.py'):
                        run(x)
                except Exception as e:
                    # print(e)
                    print('Opps!')

            for i in s:
                if i.endswith('.py'):
                    os.remove(i)