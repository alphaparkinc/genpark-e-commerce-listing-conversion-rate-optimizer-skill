from client import ECommerceListingConversionRateOptimizerClient

def main():
    client = ECommerceListingConversionRateOptimizerClient()
    res = client.optimize_listing({"name": "GaN Charger 65W", "brand": "GenPark Tech"}, ["Love how compact it is!"])
    print(f"Optimized Title: {res['optimized_title']}")
    print(f"Projected CTR Boost: +{res['projected_ctr_boost_pct']}%")

if __name__ == "__main__":
    main()
