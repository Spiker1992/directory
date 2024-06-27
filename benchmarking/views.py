from django.http import HttpResponse

import uuid
from listing_management.event_stores.listing import ListingEventStore
# from listing_management.read_models.listings import ListingTest

# Vladislavs-MBP:directory vladislavogir$ wrk -t1 -c1 -d30s http://127.0.0.1:8000/test/read
# Running 30s test @ http://127.0.0.1:8000/test/read
#   1 threads and 1 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency     7.56ms   13.56ms 172.31ms   93.73%
#     Req/Sec   209.59     71.72   300.00     72.82%
#   6255 requests in 30.09s, 1.85MB read
# Requests/sec:    207.90
# Transfer/sec:     62.94KB
def test_read_view(request):
    event = read_data()
    return HttpResponse(event)

# Vladislavs-MBP:directory vladislavogir$ wrk -t12 -c40 -d30s http://127.0.0.1:8000/test/write
# Running 30s test @ http://127.0.0.1:8000/test/write
#   12 threads and 40 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency   186.96ms  339.75ms   1.96s    86.40%
#     Req/Sec    26.77     26.54   180.00     83.18%
#   5111 requests in 30.04s, 4.82MB read
#   Socket errors: connect 0, read 19, write 0, timeout 136
#   Non-2xx or 3xx responses: 23
# Requests/sec:    170.12
# Transfer/sec:    164.19KB
def test_write_view(request):
    event = write_data()
    return HttpResponse(event)

def read_data():
    events = ListingEventStore.objects.all()
    return events.first()

def write_data():
    event = ListingEventStore(event_type="listing_created", event_payload={}, stream_id=uuid.uuid4())
    event.save()

    return event

# Vladislavs-MBP:directory vladislavogir$ wrk -t12 -c40 -d30s http://127.0.0.1:8000/test/write_postgres
# Running 30s test @ http://127.0.0.1:8000/test/write_postgres
#   12 threads and 40 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency   505.80ms  136.55ms   1.13s    68.93%
#     Req/Sec     7.26      4.64    20.00     84.19%
#   2108 requests in 30.08s, 631.99KB read
#   Socket errors: connect 0, read 14, write 0, timeout 0
# Requests/sec:     70.09
# Transfer/sec:     21.01KB
# def test_write_postgres_view(request):
#     event = ListingTest(title="listing_created", description="lorem")
#     event.save()
#     return HttpResponse(event)

# Vladislavs-MBP:directory vladislavogir$ wrk -t12 -c400 -d30s http://127.0.0.1:8000/test/read_postgres
# Running 30s test @ http://127.0.0.1:8000/test/read_postgres
#   12 threads and 400 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency     1.33s   501.00ms   2.00s    63.89%
#     Req/Sec     7.35      6.06    40.00     76.20%
#   1652 requests in 30.08s, 490.44KB read
#   Socket errors: connect 0, read 1278, write 210, timeout 1580
# Requests/sec:     54.92
# Transfer/sec:     16.31KB
# def test_read_postgres_view(request):
#     events = ListingTest.objects.all()
#     return HttpResponse(events.first())

# Vladislavs-MBP:directory vladislavogir$ wrk -t1 -c1 -d30s http://127.0.0.1:8000/test/read_blank
# Running 30s test @ http://127.0.0.1:8000/test/read_blank
#   1 threads and 1 connections
#   Thread Stats   Avg      Stdev     Max   +/- Stdev
#     Latency     2.83ms    7.84ms  99.54ms   94.69%
#     Req/Sec   812.99    276.59     1.15k    67.56%
#   24270 requests in 30.04s, 6.78MB read
# Requests/sec:    807.84
# Transfer/sec:    231.15KB
def test_blank_view(request):
    return HttpResponse("Hello World")