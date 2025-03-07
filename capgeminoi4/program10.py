# file=open('sample.txt',"w")
# file.write("hello,this is sample text")
# file.close
# with open("file.txt","w") as file:
#     file.write("hello, this is sample text")

#read the file
# with open("file.txt","r") as file:
#     file=file.read()
#     print(file)
# with open("sample.txt","r") as file:
#     for i in file:
#         print(i.strip())
# import csv
# data=[
#     {"name":"shanmuk","age":19},
#     {"name":"sai","age":20}
# ]

# csv_file="output.csv"

# with open(csv_file,mode="w",newline="") as file:
#     writer=csv.DictWriter(file,fieldnames=data[0].keys())
#     writer.writeheader()
#     writer.writerows(data)

# with open(csv_file,mode="r",newline="") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print(row)

# importing the data into csv using class
# class CSVHandler:
#     def __init__(self,data,filename):
#         self.data=data
#         self.filename=filename
#     def write(self):
#         import csv
#         csv_file=self.filename
#         with open(csv_file,mode="w",newline="") as file:
#             writer=csv.DictWriter(file,fieldnames=self.data[0].keys())
#             writer.writeheader()
#             writer.writerows(self.data)
#     def read(self):
#         import csv
#         csv_file=self.filename
#         with open(csv_file,mode="r",newline="") as file:
#             reader=csv.DictReader(file)
#             for row in reader:
#                 print(row)
# data=[
#     {"name":"shanmuk","age":19},
#     {"name":"sai","age":20}
# ]
# csv=CSVHandler(data,"output.csv")
# csv.write()
# csv.read()
# def get_input():
#     data={}
#     name=input("Enter your name:")
#     age=int(input("Enter your age:"))
#     data["name"]=name
#     data["age"]=age
#     return data
# def main():
#     data=[]
#     while True:
#         print("\n1. Add data")
#         print("2. Read data")
#         print("3. Exit")
#         choice=int(input("Enter your choice:"))
#         if choice==1:
#             data.append(get_input())
#             csv=CSVHandler(data,"output.csv")
#             csv.write()
#             print("Data added successfully")
#         elif choice==2:
#             csv=CSVHandler(data,"output.csv")
#             csv.read()
#             print("\nData read successfully")
#         elif choice==3:
#             break
#         else:
#             print("Invalid choice")
# main()
# import threading
# import time
# def single_task():
#     print("Task started")
#     time.sleep(2)
#     print("Task stopped")
# time.sleep(2)
# thread=threading.Thread(target=single_task)
# print('Main Thread')
# thread.start()
# thread.join()
# import threading
# import time
# def download_file(file_name):
#     print(f"Downloading {file_name}...")
#     time.sleep(5)
#     print(f"Downloaded {file_name}")
# files=["file1.pdf","file2.pdf","file3.pdf"]
# threads=[]
# for file in files:
#     thread=threading.Thread(target=download_file,args=(files,))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()
# print("All pdfs downloaded")
# implementing thread for even and odd
# import threading
# import time
# event=threading.Event()
# def even(n):
#     for i in range(n):
#         if i%2==0:
#             print(f"Even number: {i}")
#             time.sleep(1)
#             event.set()
#             event.clear()
# def odd(n):
#     for i in range(n):
#         if i%2==1:
#             print(f"Odd number: {i}")
#             time.sleep(1)
#             event.set()
#             event.clear()
# n=int(input())
# even_thread=threading.Thread(target=even,args=(n,))
# odd_thread=threading.Thread(target=odd,args=(n,))
# even_thread.start()
# odd_thread.start()
# even_thread.join()
# odd_thread.join()
# import threading
# import time
# import requests
# def scrape_website(url,results):
#     response=requests.get(url)
#     html_content=response.text
#     results.append(f"fetched data from {url} and response is {html_content}")
# url=[
#     "https://www.linkedin.com/feed/"
# ] 
# results=[]
# threads=[]
# for site in url:
#     thread=threading.Thread(target=scrape_website,args=(site,results))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()
# with open("context.html","w",encoding='utf-8') as file:
#         for result in results:
#              file.write(result)
# downloading files:
# import threading
# import requests
# def download_file(url,filename):
#     response=requests.get(url)
#     if response.status_code==200:
#         with open(filename,"wb") as file:
#             file.write(response.content)
#         print(f"{filename} downloaded successfully")
#     else:
#         print(f"Failed to download {filename}")
# pdfs=[
#     ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf","dummy.pdf")
# ]
# threads=[]
# for i,j in pdfs:
#     thread=threading.Thread(target=download_file,args=(i,j))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()
# import threading
# data_chunks=[
#     list(range(10)),
#     list(range(10,20)),
#     list(range(20,30))
# ]
# def process_data(chunk):
#     print(f"Processing chunk {chunk}")
#     result=sum(chunk)
#     print(f"Chunk {chunk} processed successfully and result is {result}")
# threads=[]
# for chunk in data_chunks:
#     thread=threading.Thread(target=process_data,args=(chunk,))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()
# import threading
# import time
# import queue
# def producer(q):
#     for i in range(10):
#         q.put(i)
#         print(f"Produced {i}")
#         time.sleep(1)
# def consumer(q):
#     while True:
#         item=q.get()
#         if item is None:
#             break
#         print(f"Consumed {item}")
#         time.sleep(1)

# q=queue.Queue()
# producer_thread=threading.Thread(target=producer,args=(q,))
# consumer_thread=threading.Thread(target=consumer,args=(q,))
# producer_thread.start()
# consumer_thread.start()
# producer_thread.join()
# q.put(None)
# consumer_thread.join()
# print("thread communication is completed")
# import threading
# import time
# def task(lock):
#     with lock:
#         print(f"{threading.current_thread().name} is trying to acquire lock")
#         time.sleep(2)
#         print(f"{threading.current_thread().name} has acquired lock")
# lock=threading.Lock()
# thread1=threading.Thread(target=task,args=(lock,))
# thread2=threading.Thread(target=task,args=(lock,))
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

#implementing daemon
import threading
import time
def task():
    for i in range(10):
        print(f"Task {i}")
        time.sleep(1)
thread=threading.Thread(target=task,daemon=True)
thread.start()
time.sleep(12)
print("Main thread excuting")
