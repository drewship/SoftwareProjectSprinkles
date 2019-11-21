//
//  ViewController.swift
//  CCEventsApp
//
//  Created by Sophia Quick on 11/20/19.
//  Copyright © 2019 Sophia Quick. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var whatTextField: UITextField!
    @IBOutlet weak var timeTextField: UITextField!
    @IBOutlet weak var locationTextField: UITextField!
    @IBOutlet weak var descriptionTextField: UITextField!
    
    @IBOutlet weak var titleTextView: UITextView!
    @IBOutlet weak var timeTextView: UITextView!
    @IBOutlet weak var locationTextView: UITextView!
    @IBOutlet weak var descriptionTextView: UITextView!
    
    @IBAction func submitButton(_ sender: UIButton) {
          let titleText = whatTextField.text
          let timeText = timeTextField.text
          let locationText = locationTextField.text
          let descriptionText = descriptionTextField.text
          
          titleTextView.text = titleText
          timeTextView.text = timeText
          locationTextView.text = locationText
          descriptionTextView.text = descriptionText
          
      }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

  
    
}

