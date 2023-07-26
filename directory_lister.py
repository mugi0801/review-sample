import os

class DirectoryLister:
    """_summary_
    """
    def __init__(self, directory_path):
        """_summary_

        Args:
            directory_path (str): _description_
        """
        self.directory_path = directory_path
    
    def get_directory_contents(self):
        """_summary_

        Returns:
            str: _description_
        """
        try:
            # 指定されたディレクトリ内の一覧を取得
            contents = os.listdir(self.directory_path)
            return contents
        except FileNotFoundError:
            print("指定されたディレクトリが存在しません。")
            return []