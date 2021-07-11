from django.shortcuts import render
import wolframalpha
import wikipedia


def bot_view(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client("")
        res = client.query(query)
        ans = next(res.results.text)
        return render(request, 'search_bot/search_bot.html', {'ans': ans, 'query': query})

    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'search_bot/search_bot.html', {'ans': ans, 'query': query})

        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'search_bot/search_bot.html', {'ans': ans, 'query': query})



