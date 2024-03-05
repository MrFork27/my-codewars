async function submitOrder(user) {
  let shoppingCart, zipCode, shippingRate, orderSuccessful, profile;
  
  // Get the current user's shopping cart
  shoppingCart = await OrderAPI.getShoppingCartAsync(user)
  
  // Also look up the ZIP code from their profile
  profile = await CustomerAPI.getProfileAsync(user)
  zipCode = profile.zipCode
  
  // Calculate the shipping fees
  shippingRate = calculateShipping(shoppingCart, zipCode);
  
  // Submit the order
  orderSuccessful = OrderAPI.placeOrderAsync(shoppingCart, shippingRate)
  
  console.log(`Your order ${orderSuccessful? "was" : "was NOT"} placed successfully`);
}