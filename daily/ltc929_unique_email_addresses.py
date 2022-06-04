# https://leetcode.cn/problems/unique-email-addresses/

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = set()
        for email in emails:
            e = self.filteremail(email)
            unique_email.add(e)
        print(unique_email)
        return len(unique_email)

    def filteremail(self, email):
        tmp_str = ""
        plus_tag = False
        for i in range(len(email)):
            if email[i] == "@":
                tmp_str += email[i:]
                return tmp_str
            if email[i] == "." or plus_tag:
                continue
            if email[i] == "+":
                plus_tag = True
                continue
            tmp_str += email[i]
