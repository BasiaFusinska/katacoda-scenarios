You can test how the model performs by producing the predictions and checking them with the underlying truths. With the more data though, it's much more practical to calculate some statistics.

The most obvious one is [accuracy](https://en.wikipedia.org/wiki/Accuracy_and_precision), which is the fraction of how many times the model was right. There are other metrics, but for the sake of simplicity, we'll use accuracy only. We're going to calculate it for both training and test set. Those observations can help you further with deciding about tuning your algorithm or resolving the [bias-variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff).

It looks like our algorithms performed quite well. But to be fair, we were running it on the very simple dataset. Next scenario will show you a couple of shortcomings if you are using lees nicely shaped data.
