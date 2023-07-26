
import logging
#import directory_lister
import directory_lister

def main():
    logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",filename="test.log")
    logging.info("プログラム開始")
    # 一覧取得
    directory_lister_obj = directory_lister.DirectoryLister("pyWhisper")
    # インスタンスのメソッドを使用してディレクトリの一覧を取得
    directory_contents = directory_lister_obj.get_directory_contents()
    for f in directory_contents:
        print(f)
    
if __name__ == "__main__":
    main()
