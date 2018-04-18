class Halving:
    def oneStep(self, num):
        Hash = {}
        Queue = [(num, 0)]
        Len = 1
        while Len > 0:
            # Pop Element
            (number, cnt) = Queue[0]
            del Queue[0]
            Len -= 1

            if number not in Hash:
                Hash[number] = cnt
            else:
                Hash[number] = min(Hash[number], cnt)

            if int(number / 2) not in Hash or Hash[int(number / 2)] > cnt + 1:
                Hash[int(number / 2)] = cnt + 1
                Queue.append((int(number / 2), cnt + 1))
                Len += 1

            if number % 2 == 1 and ((int(number / 2) + 1) not in Hash or Hash[int(number / 2) + 1] > cnt + 1):
                Hash[int(number / 2) + 1] = cnt + 1
                Queue.append((int(number / 2) + 1, cnt + 1))
                Len += 1
        return Hash

    def minSteps(self, a):
        Hash = None
        for number in a:
            new_Hash = self.oneStep(number)
            if Hash == None:
                Hash = new_Hash
                for key in Hash:
                    Hash[key] = [Hash[key]]
            else:
                for key in new_Hash:
                    if key in Hash:
                        Hash[key] += [new_Hash[key]]

        MIN = 1000000000000

        for key in Hash:
            if len(Hash[key]) == len(a):
                MIN = min(MIN, sum(Hash[key]))

        return MIN



A = Halving()
A.minSteps([13, 13, 7, 11, 13, 11])