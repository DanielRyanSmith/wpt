def main(request, response):
    report_id = request.GET.first(b"id", b"")
    endpoint_name = request.GET.first(b"endpoint_name", b"default")
    # Using relative URL for the endpoint as it is same-origin
    endpoint = b"/reporting/resources/report.py?op=put&reportID=" + report_id

    headers = [
        (b"Reporting-Endpoints", b"%s=\"%s\"" % (endpoint_name, endpoint)),
        (b"Content-Type", b"text/html")
    ]

    body = b"""<!doctype html>
<meta charset="utf-8">
<script>
  if (window.crashReport) {
    window.crashReport.initialize(1024).then(() => {
      window.crashReport.set('test', 'data');
    });
  }
</script>
<p>Crash me!</p>
"""
    return (200, headers, body)
