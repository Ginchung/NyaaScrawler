class Image:

    # 依據domain 呼叫不同的function
    def getImage(self, domain,url):
        def func_not_found():  # just in case we dont have the function
            print("No Function " + domain + " Found!")

        func_name = 'func_' + domain
        func = getattr(self, func_name, func_not_found)
        func()

    def func_imgbabes(self):
        pass

    def func_imgur(self):
        pass
