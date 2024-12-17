# todo: 工具包
#
# @Time: 2024/12/17 14:20:00
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import logging
import os
from typing import Any


class Tools(object):
    @staticmethod
    def get_root_dir() -> str:
        """
        获得根目录
        :return: str
        """
        # 获取当前工作目录
        current_dir = os.getcwd()
        # 获取根目录
        # root_dir = os.path.dirname(current_dir)
        return current_dir

    @staticmethod
    def create_dir(dir_path: str) -> str:
        """
        创建目录
        @param dir_path:
        @return:
        """
        if not os.path.exists(dir_path):
            # 创建目录
            os.makedirs(dir_path)
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.error(f"create {dir_path} success!")

        return dir_path

    @staticmethod
    def has_next(gen: object) -> bool:
        """
        判断生成器是否还有下一个元素
        @param gen:
        @return:
        """
        try:
            next(gen)
            return True
        except StopIteration:
            return False
            pass

    @staticmethod
    def get_list_element(lst: list, index: int) -> Any:
        """
        获取列表中的元素
        @param lst: 列表
        @param index: 列表的下标
        @return:
        """
        try:
            return lst[index]
        except IndexError:
            return None
            pass

    @staticmethod
    def get_dict_element(dic: dict, key: str) -> Any:
        """
        获取字典中的元素
        @param dic: 字典
        @param key: 字典对应的key
        @return:
        """
        try:
            return dic[key]
        except KeyError:
            return None
            pass

    @staticmethod
    def open_stealth_js() -> str:
        with open(Tools.get_root_dir() + "\\stealth.min.js", "r") as f:
            js = f.read()
        return js

    pass

if __name__ == "__main__":
    print(Tools.get_root_dir())