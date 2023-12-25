
Pytest decoratorları, pytest çerçevesinde test fonksiyonlarının veya test sınıflarının davranışını değiştiren özel fonksiyonlardır.
Bunlar @pytest.<decorator_adı> şeklinde başlar ve test sürecini geliştirmek için çeşitli işlevsellikler sunarlar.


Pytest'teki decoratorlar farklı görevler gerçekleştirebilir:

1-Fixture Oluşturma: @pytest.fixture, test fonksiyonlarının çalışması için gerekli kaynakları hazırlayan, test verileri sağlayan veya işlemler gerçekleştiren "fixture"ları oluşturmak için kullanılır.

2-Testleri İşaretleme: @pytest.mark, testleri veya test fonksiyonlarını özel işaretlerle işaretlemenizi sağlar. Bu işaretler, testleri seçmeli olarak çalıştırmanızı, kategorize etmenizi veya filtrelemenizi sağlar.

3-Parametre ile Testler: @pytest.mark.parametrize, aynı test fonksiyonunun farklı parametre setleriyle çalıştırılmasına olanak tanır, parametre ile test etmeyi mümkün kılar.

4-Testleri Atlama: @pytest.mark.skip ve @pytest.mark.skipif, test fonksiyonlarını koşmayı koşullu veya koşulsuz olarak atlamak için kullanılır.

5-Beklenen Başarısızlıklar: @pytest.mark.xfail, başarısız olması beklenen testleri işaretler, böylece bunlar beklenen başarısızlık olarak çalıştırabilir ve raporlanabilir.
