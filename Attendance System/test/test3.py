import process
import opencv


try:
    a=process.search('icon.jpg')
    print(a)
except opencv.fr.api_error.APIError:
    print('Not Found')