# from presidio_anonymizer import AnonymizerEngine
# from presidio_analyzer import AnalyzerEngine
import string
import secrets


def generate_random_string(length, uppercase=False, method='hex', urlsafe=True):
    if length < 1:
        length = 10

    if method == 'hex' and urlsafe:
        return secrets.token_urlsafe(length // 2)
    elif method == 'hex' and not urlsafe:
        return secrets.token_hex(length)
    elif method == 'ascii':
        return str(''.join(
            secrets.choice((string.ascii_uppercase if uppercase else string.ascii_lowercase) + string.digits) for i in
            range(length)))


def get_ip_from_request(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


# def mask_personally_identifiable_information(text):
#     analyzer = AnalyzerEngine()
#     detections = analyzer.analyze(text=text, language="en")
#     engine = AnonymizerEngine()
#     result = engine.anonymize(
#         text=text,
#         analyzer_results=detections,
#     )
#     return result
