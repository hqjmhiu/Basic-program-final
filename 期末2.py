def search_and_print(file_path, search_string):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if search_string in line:
                    print(line.strip())  

    except FileNotFoundError:
        print(f"找不到檔案：{file_path}")
    except Exception as e:
        print(f"發生錯誤：{e}")


file_path = 'python.excel.csv'
search_string = '英文(一)'


search_and_print(file_path, search_string)