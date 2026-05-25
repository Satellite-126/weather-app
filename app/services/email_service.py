import resend
import os

resend.api_key = os.getenv("RESEND_API_KEY")

#Email HTML Structure
def generate_email_html(weather_data):
    # Dictionary mapping conditions to high-quality Unsplash illustration URLs
    weather_images = {
        "clear": "https://images.unsplash.com/photo-1504386106331-3e4e71712b38?q=80&w=600&auto=format&fit=crop", # Sunny/Clear
        "clouds": "https://images.unsplash.com/photo-1534088568595-a066f410bcda?q=80&w=600&auto=format&fit=crop", # Cloudy
        "rain": "https://images.unsplash.com/photo-1534274988757-a28bf1a57c17?q=80&w=600&auto=format&fit=crop", # Rainy
        "snow": "https://images.unsplash.com/photo-1491002052546-bf38f186af56?q=80&w=600&auto=format&fit=crop", # Snowy
        "thunderstorm": "https://images.unsplash.com/photo-1605727216801-e27ce1d0cc28?q=80&w=600&auto=format&fit=crop" # Storm
    }

    # Base container with background shading and standard email client fixes
    html = """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Daily Weather Report</title>
      </head>
      <body style="margin: 0; padding: 40px 0; background-color: #f4f6f9; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          
          <tr>
            <td align="center" style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 40px 20px;">
              <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 700; letter-spacing: -0.5px;">/ Weather Forecast /</h1>
              <p style="margin: 8px 0 0 0; color: #bfdbfe; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Your Automated Daily Update</p>
            </td>
          </tr>

          <tr>
            <td style="padding: 30px 24px;">
    """

    # Generate an elegant, standalone "Card" for each city
    for item in weather_data:
        condition_lower = item['condition'].lower()
        
        # Match condition keywords to our image bank (fallback to a generic cloudy image)
        bg_image = weather_images.get("clouds")
        for key in weather_images:
            if key in condition_lower:
                bg_image = weather_images[key]
                break

        html += f"""
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-bottom: 24px; border: 1px solid #e5e7eb; border-radius: 12px; overflow: hidden; border-collapse: separate;">
                <tr>
                  <td width="30%" valign="middle" style="background-image: url('{bg_image}'); background-size: cover; background-position: center; min-height: 120px;">
                    <div style="height: 120px;"></div>
                    </td>
                  
                  <td width="70%" style="padding: 20px; background-color: #ffffff; vertical-align: middle;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                      <tr>
                        <td>
                          <h2 style="margin: 0; font-size: 22px; color: #1f2937; font-weight: 600;">{item['city']}</h2>
                          <p style="margin: 4px 0 12px 0; font-size: 14px; color: #6b7280; text-transform: capitalize;">✨ {item['condition']}</p>
                        </td>
                        <td align="right" valign="top">
                          <span style="font-size: 28px; font-weight: 800; color: #2563eb;">{item['temperature']}°C</span>
                        </td>
                      </tr>
                      <tr>
                        <td colspan="2" style="border-top: 1px dashed #e5e7eb; padding-top: 12px;">
                          <p style="margin: 0; font-size: 13px; color: #4b5563; font-style: italic; line-height: 1.4;">
                            <strong>AI Analysis:</strong> {item.get('feel', 'No extra commentary generated for today.')}
                          </p>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
              """

    # Footer section closeout
    html += """
            </td>
          </tr>
          
          <tr>
            <td align="center" style="background-color: #f9fafb; padding: 24px; border-top: 1px solid #f3f4f6;">
              <p style="margin: 0; font-size: 12px; color: #9ca3af;">This email has been sent to you by OpenWeather and Resend.</p>
            </td>
          </tr>

        </table>
      </body>
    </html>
    """

    return html

#Email Send
def send_email(to_email, html):

    try:
        response = resend.Emails.send({
            "from": "Weather Alert <onboarding@resend.dev>",
            "to": to_email,
            "subject": "Daily Weather Report",
            "html": html
        })

        print("EMAIL SENT:", response)

    except Exception as e:
        print("EMAIL ERROR:", str(e))
        raise e