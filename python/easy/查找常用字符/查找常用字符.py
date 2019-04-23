class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        import functools as func
        return list(func.reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())
        #此处注意，python3已经没有reduce关键字，需要通过引入functools的reduce方法来解决，作用是对提供的参数一（函数方法）和参数二（运算）合二为一
        #__and__魔法属性用来统计重复字符，并且以字典的形式给出
        #elements（）：获取elements就是将其中的key值乘以出现次数全部打印出来，当然需要通过list或者其他方式将其所有元素全部展示出来，当出现了负数或者0的情况，可以看到：负数对应的key值是不会打印的。
        #func.reduce(collections.Counter.__and__, map(collections.Counter, A)).elements()单独打印是一个itertools，即<itertools.chain object at 0x7fab10461978>
        #map（）函数，第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。第二个参数为iterable（一个或者多个的序列）
