from django.shortcuts import render


def main(requests):
    return render(requests, 'HomePage/index.html')
