from user.models.block import BlockMail
from user.models.block import BlockNumber
def block_mail(mail,number):
    
    if (BlockMail.objects.filter(blockmail=mail).exists()) or (BlockNumber.objects.filter(blocknumber=number).exists()) :
        return True
         
    else:
        return False
