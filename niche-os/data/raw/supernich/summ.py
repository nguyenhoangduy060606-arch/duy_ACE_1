import json,sys,datetime as dt
f=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 60
d=json.load(open(f)); vs=d.get('videos',d)
for v in vs[:n]:
    t=dt.datetime.utcfromtimestamp(v['videoPublishedAt']).strftime('%m-%d') if v.get('videoPublishedAt') else ''
    print(f"{v['channelTitle'][:22]:22}|{v.get('subscriberCount',0):>8}|{v['viewCount']:>9}|x{(v.get('breakoutScore') or 0):<8.0f}|{(v.get('videoDuration') or 0)//60:>4}m|{t}| {v['videoTitle'][:100]}")
